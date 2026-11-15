#include "audio_manager.hpp"
#include "network_manager.hpp"
#include <spdlog/spdlog.h>

audio_manager::audio_manager()
{
    _format = std::make_unique<AudioFormat>();
}

audio_manager::~audio_manager() = default;

void audio_manager::start_loopback_recording(std::shared_ptr<network_manager> network_manager, const capture_config& config)
{
    _stopped = false;
    _capture_failed = false;
    _record_thread = std::thread([network_manager = network_manager, config = config, self = shared_from_this()] {
        try {
            self->do_loopback_recording(network_manager, config);
        } catch (const std::exception& e) {
            spdlog::error("Audio capture failed: {}", e.what());
        }
        if (!self->_stopped) {
            self->_capture_failed = true;
            network_manager->request_stop();
        }
    });
}

void audio_manager::stop()
{
    _stopped = true;
    if (_record_thread.joinable()) {
        _record_thread.join();
    }
}

bool audio_manager::capture_failed() const
{
    return _capture_failed;
}

std::string audio_manager::get_format_binary()
{
    return _format->SerializeAsString();
}