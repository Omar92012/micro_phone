def on_forever():
    led.plot_bar_graph(input.sound_level(), 0)
forever(on_forever)
