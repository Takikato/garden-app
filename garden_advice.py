# Hardcoded values for the season and plant type
season = input("Please enter a season (e.g summer): ").lower().strip()
plant_type = input("Please enter plant type (e.g flower): ").lower().strip()

# Determine advice based on the season
season_info = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n"
}

plant_info = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

if season in season_info:
    advice = season_info[season]

else:
    advice = "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type in plant_info:
    advice += plant_info[plant_type]

else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)
