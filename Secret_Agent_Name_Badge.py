# Part 1: Ask agent their details
name  = input ("Enter your real name, Agent: ")
gadget = input ("Enter your favourite gadget: ")

# print(name)
# print(gadget)

#  Part 2: Strore Agent details using different date type
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.5
is_active = True

# Print each details with it data type
# print ("name: ", name , " -> type: ", type (name))
# print("gadget: ", gadget , "-> type ", type (gadget))
#print("agent_number: ", agent_number, "-> type ", type (agent_number))
#print("mission_count: ", mission_count, "-> type ", type (mission_count))
#print("height: ", height_m, "-> type ", type (height_m))
#print("is_active: ", is_active, "-> type ", type (is_active))

# Part 4 Typecast the number and true and false value into text
agent_number_text = str(agent_number)
speed_rating_text = str(speed_rating)
mission_count_text = str(mission_count)
status_text = str(is_active)

print("Agent Number as text", agent_number_text, "-> type", type(agent_number_text))
print("Agent Number as Number", agent_number, "-> type", type(agent_number))
print("speed rating as text", speed_rating_text, "-> type", type(speed_rating_text))
print("mission_count_text as text", mission_count_text, "-> text", type(mission_count_text))
print("status_text as text", is_active, "-> type", type(status_text))

# slicing the name to create the secret code
first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First three letter of the name", first_three)
print("Last letter is", last_letter)
print("Secret Code Name", code_name)


# Part 6 Reverse the gadget name using slicing
Reversed_gadget = gadget[::-1]
print("Reveresed Gadget Name is:", Reversed_gadget)

# Join every thing to build final badge message
badge_line_1 = "Agent: " + code_name.upper()
badge_line_2 = "ID " + agent_number_text + " | MISSION: " + mission_count_text
badge_line_3 = "SPEED: " + speed_rating_text + "| ACTIVE: " + status_text.upper()
badge_line_4 = "SECRET GADGET CODE: " + Reversed_gadget.upper()

# Print the complete Secret Agent Code
print("")
print("====== SECRET AGENT CODE======")

print (badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===============================")
