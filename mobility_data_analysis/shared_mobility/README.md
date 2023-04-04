# Transportation Data Analysis Project

This project aims to analyze transportation data by determining the origin-destination matrix of trips and showcasing relevant statistics to understand mobility patterns.

## Requirements

- Python 3.7 or higher
- The pandas, matplotlib.

## Environment Setup

1. Clone the repository to your local machine: `git clone https://github.com/yeltsinvc/OpenAITransportation`
2. Navigate to the project directory: `cd OpenAITransportation/mobility_data_analysis/shared_mobility`
3. Add `Shared_Micromobility_Vehicle_Trips.csv` in data folder

## Data
Data can be download from https://data.austintexas.gov/Transportation-and-Mobility/Shared-Micromobility-Vehicle-Trips/7d8e-dm7r

| ID                                   | Device ID                            | Vehicle Type   |   Trip Duration |   Trip Distance | Start Time             | End Time               | Modified Date          |   Month |   Hour |   Day of Week |   Council District (Start) |   Council District (End) |   Year |   Census Tract Start |   Census Tract End | Start Time (US/Central)   | End Time (US/Central)   |
|:-------------------------------------|:-------------------------------------|:---------------|----------------:|----------------:|:-----------------------|:-----------------------|:-----------------------|--------:|-------:|--------------:|---------------------------:|-------------------------:|-------:|---------------------:|-------------------:|:--------------------------|:------------------------|
| 5a23a573-418b-443b-8dc8-d7963fe2b063 | 5cee599e-832c-4fa5-9050-dcc00e3790f3 | scooter        |            2184 |        4254.48  | 11/02/2021 12:45:00 AM | 11/02/2021 01:15:00 AM | 11/03/2021 03:16:12 AM |      11 |      1 |             1 |                          9 |                        9 |   2021 |          48453001100 |        48453001100 | 11/01/2021 07:45:00 PM    | 11/01/2021 08:15:00 PM  |
| dac12ecc-0f79-4faa-a626-674a7c9f3df2 | 20014eea-19b2-4643-b3b3-63c31e76e57b | scooter        |             705 |        2670.87  | 11/02/2021 01:30:00 AM | 11/02/2021 01:30:00 AM | 11/03/2021 03:16:12 AM |      11 |      1 |             1 |                          3 |                        9 |   2021 |          48453000902 |        48453001100 | 11/01/2021 08:30:00 PM    | 11/01/2021 08:30:00 PM  |
| d6bdc5e8-dec0-4917-ab4f-5b848f61dc5e | 2cad7083-7af6-4b22-8540-9b9dfffc2f58 | scooter        |             189 |         258.939 | 11/02/2021 01:15:00 AM | 11/02/2021 01:30:00 AM | 11/03/2021 03:16:10 AM |      11 |      1 |             1 |                          1 |                        1 |   2021 |          48453001100 |        48453001100 | 11/01/2021 08:15:00 PM    | 11/01/2021 08:30:00 PM  |
| 3b17953e-9d9c-4d27-b5ac-ad76eaac2fbb | fde91af9-deb8-41cc-9ddc-472ff7653d90 | scooter        |             203 |         354.088 | 11/02/2021 01:30:00 AM | 11/02/2021 01:30:00 AM | 11/03/2021 03:16:11 AM |      11 |      1 |             1 |                          1 |                        9 |   2021 |          48453001100 |        48453001100 | 11/01/2021 08:30:00 PM    | 11/01/2021 08:30:00 PM  |
| 258bea73-5b14-4970-950e-1a1a7c3d715f | b748cae7-7f46-48a7-834d-980565210bf6 | scooter        |             166 |         757     | 01/30/2022 05:45:00 PM | 01/30/2022 05:45:00 PM | 02/08/2022 03:12:27 AM |       1 |     17 |             6 |                          9 |                        9 |   2022 |          48453000604 |        48453000603 | 01/30/2022 11:45:00 AM    | 01/30/2022 11:45:00 AM  |


## Usage

1. Run the `main.py` script to generate the origin-destination matrix and distance charts.
2. The images will be saved in the 'Results' and 'Distance' folders, respectively.

## Results
1. Matrix OD by day
<img src="Results/2018-04-05.png" alt="Matrix ID of 2018-04-05">

2. Distance diagram by day
<img src="Distance/2018-04-07.png" alt="Distance diagram of 2018-04-07">

## Contributing

1. Clone the repository to your local machine: `git clone https://github.com/username/openai-transportation.git`
2. Create a new branch for your contribution: `git checkout -b new-feature`
3. Make the necessary changes and commit your changes: `git commit -am "Add new feature"`
4. Push your changes to the repository: `git push origin new-feature`
5. Create a pull request on GitHub.

## Contact

If you have any questions or would like to contribute to this project, please contact us at ylvaleroc@gmail.com.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.