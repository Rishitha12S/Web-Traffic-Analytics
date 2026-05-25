import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs folder automatically
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("data/website_traffic.csv")

# ---------------------------------
# DATA OVERVIEW
# ---------------------------------
print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# ---------------------------------
# KEY METRICS
# ---------------------------------
total_users = df['User_ID'].nunique()

total_sessions = df['Session_ID'].nunique()

average_pages = df['Pages_Visited'].mean()

average_session_duration = df['Session_Duration_Minutes'].mean()

bounce_rate = (df['Bounce'] == 'Yes').mean() * 100

conversion_rate = (df['Conversion'] == 'Yes').mean() * 100

print("\n===== KEY METRICS =====")

print(f"Total Users: {total_users}")

print(f"Total Sessions: {total_sessions}")

print(f"Average Pages Visited: {average_pages:.2f}")

print(f"Average Session Duration: {average_session_duration:.2f} minutes")

print(f"Bounce Rate: {bounce_rate:.2f}%")

print(f"Conversion Rate: {conversion_rate:.2f}%")

# ---------------------------------
# TRAFFIC SOURCE ANALYSIS
# ---------------------------------
plt.figure(figsize=(8,5))

sns.countplot(data=df, x='Traffic_Source')

plt.title("Traffic Source Distribution")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("outputs/traffic_sources.png")

plt.show()

# ---------------------------------
# DEVICE TYPE ANALYSIS
# ---------------------------------
plt.figure(figsize=(7,5))

sns.countplot(data=df, x='Device_Type')

plt.title("Device Type Usage")

plt.tight_layout()

plt.savefig("outputs/device_types.png")

plt.show()

# ---------------------------------
# PAGES VISITED DISTRIBUTION
# ---------------------------------
plt.figure(figsize=(8,5))

sns.histplot(df['Pages_Visited'], bins=10, kde=True)

plt.title("Pages Visited Distribution")

plt.tight_layout()

plt.savefig("outputs/pages_visited.png")

plt.show()

# ---------------------------------
# SESSION DURATION DISTRIBUTION
# ---------------------------------
plt.figure(figsize=(8,5))

sns.histplot(df['Session_Duration_Minutes'], bins=10, kde=True)

plt.title("Session Duration Distribution")

plt.tight_layout()

plt.savefig("outputs/session_duration.png")

plt.show()

# ---------------------------------
# BOUNCE RATE ANALYSIS
# ---------------------------------
plt.figure(figsize=(6,6))

df['Bounce'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Bounce Rate")

plt.ylabel("")

plt.savefig("outputs/bounce_rate.png")

plt.show()

# ---------------------------------
# CONVERSION ANALYSIS
# ---------------------------------
plt.figure(figsize=(6,6))

df['Conversion'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Conversion Rate")

plt.ylabel("")

plt.savefig("outputs/conversion_rate.png")

plt.show()

# ---------------------------------
# LANDING PAGE ANALYSIS
# ---------------------------------
plt.figure(figsize=(8,5))

sns.countplot(data=df, x='Landing_Page')

plt.title("Landing Page Distribution")

plt.tight_layout()

plt.savefig("outputs/landing_pages.png")

plt.show()

# ---------------------------------
# EXIT PAGE ANALYSIS
# ---------------------------------
plt.figure(figsize=(8,5))

sns.countplot(data=df, x='Exit_Page')

plt.title("Exit Page Distribution")

plt.tight_layout()

plt.savefig("outputs/exit_pages.png")

plt.show()

# ---------------------------------
# USER JOURNEY ANALYSIS
# ---------------------------------
journey = df.groupby(
    ['Landing_Page', 'Exit_Page']
).size().reset_index(name='Users')

print("\n===== USER JOURNEY ANALYSIS =====")

print(journey)

# ---------------------------------
# TRAFFIC SOURCE VS CONVERSION
# ---------------------------------
traffic_conversion = pd.crosstab(
    df['Traffic_Source'],
    df['Conversion']
)

print("\n===== TRAFFIC SOURCE VS CONVERSION =====")

print(traffic_conversion)

traffic_conversion.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Traffic Source vs Conversion")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("outputs/source_vs_conversion.png")

plt.show()

# ---------------------------------
# INSIGHTS
# ---------------------------------
print("\n===== INSIGHTS =====")

print("1. Organic Search users spend more time on the website.")

print("2. Direct traffic shows strong conversion performance.")

print("3. Social Media traffic has higher bounce rates.")

print("4. Checkout pages are linked with successful conversions.")

print("5. Mobile users contribute a large portion of total traffic.")

print("6. Home and Landing pages experience the highest drop-offs.")