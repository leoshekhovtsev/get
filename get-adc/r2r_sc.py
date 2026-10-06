import r2r_adc as r2r
import adc_plot as plt
import time

adc=r2r.R2R_ADC(3.22, 0.0001, True)
voltage_values=[]
time_values=[]
duration=3.0

try:
    start_time=time.perf_counter()
    while (time.perf_counter() - start_time < duration):
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time.perf_counter()-start_time)
        time.sleep(0.0001)
    plt.plot_voltage_vs_time(time_values, voltage_values, max(voltage_values))
finally:
    adc.deinit()
    plt.plot_voltage_vs_time(time_values, voltage_values, max(voltage_values))
