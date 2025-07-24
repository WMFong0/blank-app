def twentyfourh_to_12h(time: str) -> str: # For str only
  time = time.split(':')
  hour = int(time[0])
  if hour >= 12:
    time.append("PM")
    if (hour > 12):
      time[0] = str(hour - 12)
  else:
    time.append("AM")
    if (hour == 0):
      time[0] = str(12)

  return ":".join(time[:-1]) + " " + time[-1]

def No_empty_string(received_data): # A useless tool
  if received_data == "":
    return None
  else: return received_data

def select_place(original_selection, raw_data_temperature_datasection: list, variable_name_for_station: str, supported_station: dict = {}): # I don't suggest you use it else where, ngl
    # Predefined
    if original_selection in supported_station.keys():
      return District_reference_for_temperature[original_selection]

    available_station = []
    # Fetch available station
    for station_data in raw_data_temperature_datasection:
      available_station.append( station_data[variable_name_for_station] )

    # Remove supported station
    for station in supported_station.values():
      available_station.remove(station)

    # Same Name Case
    if original_selection in available_station:
      return original_selection


    # Required Manual Case
    print("Since we currently doesn't support automatic selection of weather station at your district\n Please select the nearest weather station from the list below: ")
    station = ""

    while True:
      print("Available Station: ")
      for i in range(len(available_station)):
        if (i != 0 and i % 4 == 0):
          print("\t" + available_station[i], end = '\n')
        else:
          print("\t" + available_station[i], end = '')

      station = input("\nKey in your nearest Weather Station: ")
      # Just in case operation
      if (station in available_station):
        print()
        break
      print("You have input a unavailable station. Please input a available Station." + "\n"*2)
    return station
  
def lazy_list_message(message_list: list = []): # Handles and prints every message inside the list
  for message in message_list:
    message = message.replace('a.m.', 'am').replace('p.m.','pm').replace("No.", "No")
    small_message = [part.strip() for part in message.split('. ') if part.strip()]
    if not small_message:
        continue

    print(f"\t{small_message[0]}")
    for part in small_message[1:]:
      if part != "":
        if ';' in part:
          smaller_part = part.split(';')
          for text in smaller_part:
            print(f"\t\t{text}")
        else:
          print(f"\t\t{part}")

def format_name(Name: str = "") -> str: # A Error handling tool for names
  splited_name = Name.split(" ")
  for i in range(len(splited_name)):
    splited_name[i] = splited_name[i].lower().capitalize()
  return " ".join(splited_name)
