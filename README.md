# NCR_RIDE_BOOKING-
NCR Ride Analytics Dataset 2024 (UBER) The dataset comprises comprehensive ride-sharing records from Uber’s 2024 operations, offering valuable insights into booking trends, vehicle efficiency, revenue generation, cancellation patterns, and customer satisfaction.

📊 Dataset Overview
The dataset records 148,770 ride transactions across diverse vehicle segments, offering a comprehensive snapshot of Uber’s 2024 operations. It highlights ride completions, cancellation trends, customer interaction patterns, and revenue dynamics, providing actionable insights into both operational efficiency and user experience.

Data Schema
The dataset contains the following columns:

Column Name	Description
Date	Date of the booking
Time	Time of the booking
Booking ID	Unique identifier for each ride booking
Booking Status	Status of booking (Completed, Cancelled by Customer, Cancelled by Driver, etc.)
Customer ID	Unique identifier for customers
Vehicle Type	Type of vehicle (Go Mini, Go Sedan, Auto, eBike/Bike, UberXL, Premier Sedan)
Pickup Location	Starting location of the ride
Drop Location	Destination location of the ride
Avg VTAT	Average time for driver to reach pickup location (in minutes)
Avg CTAT	Average trip duration from pickup to destination (in minutes)
Cancelled Rides by Customer	Customer-initiated cancellation flag
Reason for cancelling by Customer	Reason for customer cancellation
Cancelled Rides by Driver	Driver-initiated cancellation flag
Driver Cancellation Reason	Reason for driver cancellation
Incomplete Rides	Incomplete ride flag
Incomplete Rides Reason	Reason for incomplete rides
Booking Value	Total fare amount for the ride
Ride Distance	Distance covered during the ride (in km)
Driver Ratings	Rating given to driver (1-5 scale)
Customer Rating	Rating given by customer (1-5 scale)
Payment Method	Method used for payment (UPI, Cash, Credit Card, Uber Wallet, Debit Card)


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

