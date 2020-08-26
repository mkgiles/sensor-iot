# Device Script
This script is to be run on the raspberry pi
## Magic Numbers
The script contains several magic numbers which need to be change based on the sensor used. These are rzero, rs, and ppml. In order to use this script, it is import to understand what these values represent. RS in a resistance sensor, is the resistance of the sensor component at a given moment in time. R0 is the value of RS at a specific concentration (or in fresh air). Resistance gas sensors vary along the ratio of RS/R0 in the presence of the gas being sensed, this means knowing the value of R0 is crucial to mapping ppm to the voltage being read from the ADC. The values in the assignment for PPML are derived from the datasheet. Specifically, they are obtained from the slope and intercept of the CO line in the datasheet.
The value of RS is simply the voltage the sensor is driven at (5V usually) times the Load resistance. Divided by the voltage signal and subtracting the load resistance (usually 10kΩ). As an equation: RS = VCC\*RL/VS - RL
### Obtaining R0
Knowing RS/R0 for fresh air (obtainable from the datasheet), deriving R0 is simple. Connect the sensor up, place it in a fresh air environment, and collect several hundred samples of VS. Average the VS samples and convert the result to RS. Then divide by the value of RS/R0 for fresh air.
### Obtaining PPML
RS/R0 varies according to the equation log(y) = m\*log(x)+b. Solving for x, this gives x = 10^((log(y)-b)/m).
given y = RS/R0, and x = ppm, we can split the equation into two steps. ppm = 10^ppml, and ppml = (log(rs/r0)-b)/m
b and m are the intercept and slope of the log-line equation, and can be easily worked out from the datasheet by taking two points on the CO line (or line of whatever gas you are measuring) from the graph of RS/R0 vs ppm. Substituting those values in for m and b gives the ppml equation in the code.
### Further Reading
For more information on setting up a gas sensor, see [here](https://jayconsystems.com/blog/understanding-a-gas-sensor)
## Running the script
After making sure all of the dependencies are installed, enter the details for the base station into the script.
Run script with `python3 co.py`
