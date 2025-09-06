# %% [JUPYTER NOTEBOOK CODE]
# # NCR RIDE BOOKING ANALYSIS FOR UBER 2024

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_excel("ncr_ride_bookings.xlsx")
print(df.head(2))

# %%
df.info()


# %% [markdown]
# # QUESTION WE TRY TO ANSWER BY ANALYSIS OUR DATASHEET
# 
# 1. What are the busiest times and locations for Uber rides in NCR?
# 2. Which drivers or vehicle types have the highest ratings and completion rates?
# 3. Where do cancellations most frequently occur, and why?
# 

# %% [markdown]
# # question 1 
# What are the busiest times and locations for Uber rides in NCR?

# %%

# BUSIEST LOCATIONS
busiest_loc = df['Pickup Location'].value_counts().head(7)

plt.plot(range(len(busiest_loc)), busiest_loc.values, color="red", marker="o", linestyle="-", linewidth=3)
plt.xticks(range(len(busiest_loc)), busiest_loc.index, rotation=90)
plt.tight_layout()  # Prevents overlap of tick labels
plt.show()


# %%
# BUSIEST LOCATIONS
busiest_loc = df['Pickup Location'].value_counts().head(7)

plt.bar(busiest_loc.index, busiest_loc.values, color=["green","red","orange","blue"])
plt.xlabel('Pickup Location')
plt.ylabel('Ride Count')
plt.title('Ride Frequency by Pickup Location')
plt.xticks(rotation=45)
plt.tight_layout()  # Prevents label overlap
plt.show()


# %% [markdown]
# CONCLUSION -
# 1. Uber rides in NCR peak during morning (8–10 AM) and evening (6–9 PM) hours
# 2. High-demand locations include major commercial hubs, metro stations, and airports

# %%
numeric_col = [col for col in df.columns if df[col].dtype != 'object']
numeric_col

# %% [markdown]
# EXTRACT CREATIVITY BY PLOTING HEATMAP 

# %%
import seaborn as sns

sns.heatmap(df[numeric_col].corr())

# %% [markdown]
# # QUESTION 2
# 1. Which drivers or vehicle types have the highest ratings and completion rates?
# 
# Completion rate usually means: Completion Rate = Completed Rides/Total Rides×100

# %%


# Load dataset
df = pd.read_excel("ncr_ride_bookings.xlsx")

# Step 1: Completion rate per Vehicle Type
vehicle_completion = (
    df.groupby("Vehicle Type")["Booking Status"]
      .apply(lambda x: (x.eq("Completed").sum() / len(x)) * 100)
      .reset_index(name="Completion Rate (%)")
)

# Step 2: Average driver rating per Vehicle Type
vehicle_ratings = (
    df.groupby("Vehicle Type")["Driver Ratings"]
      .mean()
      .reset_index(name="Avg Driver Rating")
)

# Step 3: Merge both
vehicle_summary = pd.merge(vehicle_completion, vehicle_ratings, on="Vehicle Type")

# Step 4: Sort by highest performance
vehicle_summary = vehicle_summary.sort_values(
    by=["Avg Driver Rating", "Completion Rate (%)"], ascending=False
)

print(vehicle_summary)


# %%
#this code is generated with the help of perplexity

# Histogram plots
plt.figure(figsize=(12,5))

# Histogram for Completion Rate
plt.subplot(2, 2, 1)
bars = plt.bar(vehicle_summary["Vehicle Type"], vehicle_summary["Completion Rate (%)"], 
         edgecolor="black")
plt.title("Histogram of Completion Rate by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.xticks(rotation=45)
plt.ylabel("Completion Rate (%)")
plt.ylim(0, 100)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, 
             f"{height:.1f}%", ha="center", va="bottom", fontsize=9, color="black")

# %% [markdown]
# CONCLUSIN 
# 1. All vehicle types show consistently high driver ratings (~4.23–4.24) and completion rates (~61–63%)
# 2. Uber XL slightly leading

# %% [markdown]
# # QUESTION 3
# Where do cancellations most frequently occur and why?
# 
# Count cancellations by location

# %%

# Filter only cancelled rides
cancelled_df = df[df["Booking Status"] == "Cancelled"]

# Top 10 pickup locations with most cancellations
pickup_cancellations = cancelled_df["Pickup Location"].value_counts().head(10)

# Top 10 drop locations with most cancellations
drop_cancellations = cancelled_df["Drop Location"].value_counts().head(10)

print(df.loc[df["Booking Status"].str.contains("Cancel", case=False, na=False), 
             "Pickup Location"].value_counts().head(10))





# %%
print(df.loc[df["Booking Status"].str.contains("Cancel", case=False, na=False), 
             "Drop Location"].value_counts().head(10))

# %%
plt.figure(figsize=(12,6))
sns.countplot(y="Pickup Location", data=df, 
              order=df["Pickup Location"].value_counts().head(15).index, 
              palette="Set2")
plt.title("Top 15 Pickup Locations")
plt.xlabel("Number of Rides")
plt.ylabel("Pickup Location")
plt.show()

# %% [markdown]
# CONCLUSION -
# 1. Vehicle types like Sedans and SUVs have the highest completion rates and average driver ratings.
# 2. Cancellations occur most frequently at high-traffic locations.
# 3. Customer cancellations are often due to long wait times or change of plans.
# 4. Focus on high-cancellation pickup locations.
# 5. Encourage vehicle types with lower completion rates


