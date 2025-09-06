# NCR_RIDE_BOOKING-
NCR Ride Analytics Dataset 2024 (UBER) The dataset comprises comprehensive ride-sharing records from Uber’s 2024 operations, offering valuable insights into booking trends, vehicle efficiency, revenue generation, cancellation patterns, and customer satisfaction.

📊 Dataset Overview
The dataset records 148,770 ride transactions across diverse vehicle segments, offering a comprehensive snapshot of Uber’s 2024 operations. It highlights ride completions, cancellation trends, customer interaction patterns, and revenue dynamics, providing actionable insights into both operational efficiency and user experience.

Data Schema
The dataset contains the following columns:

Column Name	Description
1.Date	Date of the booking

2.Time	Time of the booking

3.Booking ID	Unique identifier for each ride booking

4.Booking Status	Status of booking (Completed, Cancelled by Customer, Cancelled by Driver, etc.)

5.Customer ID	Unique identifier for customers

6.Vehicle Type	Type of vehicle (Go Mini, Go Sedan, Auto, eBike/Bike, UberXL, Premier Sedan)

7.Pickup Location	Starting location of the ride

8.Drop Location	Destination location of the ride

9.Avg VTAT	Average time for driver to reach pickup location (in minutes)

10.Avg CTAT	Average trip duration from pickup to destination (in minutes)

11.Cancelled Rides by Customer	Customer-initiated cancellation flag


12.Reason for cancelling by Customer	Reason for customer cancellation

13.Cancelled Rides by Driver	Driver-initiated cancellation flag

14.Driver Cancellation Reason	Reason for driver cancellation

15.Incomplete Rides	Incomplete ride flag

16.Incomplete Rides Reason	Reason for incomplete rides

17.Booking Value	Total fare amount for the ride

18.Ride Distance	Distance covered during the ride (in km)

19.Driver Ratings	Rating given to driver (1-5 scale)

20.Customer Rating	Rating given by customer (1-5 scale)

21.Payment Method	Method used for payment (UPI, Cash, Credit Card, Uber Wallet, Debit Card)



Revenue Distribution by Payment Method
UPI: Highest contributor (~40% of total revenue)
Cash: Second highest (~25% of total revenue)
Credit Card: ~15% of total revenue
Uber Wallet: ~12% of total revenue
Debit Card: ~8% of total revenue

📈 Data Quality
Completeness: Comprehensive coverage with minimal missing values
Consistency: Standardized vehicle types and status categories
Temporal Coverage: Full year 2024 data with daily granularity
Geographic Scope: Multiple pickup and drop locations
Balanced Distribution: Good representation across all vehicle types and time periods.

