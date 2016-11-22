from RPIO import PWM

PWM.setup()
PWM.init_channel(0)

PWM.add_channel_pulse(0, 12, 0, 50)
PWM.add_channel_pulse(0, 12, 100, 50)

PWM.clear_channel_gpio(0, 12)

input('waiting...')
PWM.cleanup()
