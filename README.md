# Indoor-positioning-system

This project uses WiFi signal strength from various fixed nodes in order to calculate the user's position in real-time. The advantage over GPS is that this can be used for short-range positioning, like in a building/mall. To serve as Wi-Fi nodes, we use ESP8266 modules, a family of Wi-Fi chips with a microcontroller unit inbuilt. One ESP module is used as a station, which measures the signal strength from the other ESPs (Access points). This station ESP uploads the retrieved data on to a web page.
Then we download the data on a computer, process it and pinpoint the location of the station ESP, relative to the access points.
Calibration of signal strength vs distance, Calculations on the data and plotting of the final location are done using Python.

The curve fitting of the obtained values of signal strength vs distance is one of the major calculations involved. Here is the link for the method we applied to achieve this
http://mathworld.wolfram.com/LeastSquaresFittingPowerLaw.html
<img width="818" alt="Screenshot 2022-01-23 at 1 35 24 PM" src="https://user-images.githubusercontent.com/19953916/150669903-595f1719-6215-477b-9f08-dac4196ba229.png">

Here is picture of the output of the positioning algorithm. This shows how the algorithm calculates the point of intersection of the circles.

<img width="592" alt="Screenshot 2022-01-23 at 1 33 43 PM" src="https://user-images.githubusercontent.com/19953916/150669864-fa8c41c7-9009-4677-8dbc-ed4df1bd1d87.png">

For circles which are not intersecting the figure is shown below. We observe that the point shown by the algorithm is on the locus of those points which we would get if the radii of the circle were kept on increasing till they intersect. Hence, we get a good approximation in real time scenarios even when the circles are not intersecting.

<img width="668" alt="Screenshot 2022-01-23 at 1 37 23 PM" src="https://user-images.githubusercontent.com/19953916/150669941-0a6a0ec5-befc-4b9c-a1de-a760fb28adac.png">

Please refer to detailed documentation attaached
