def display_result(source,destination,distance,mode): #currency,langlist,callingcode):
    print()
    print(f"✈️  TRIP SUMMARY: {source.capitalize()} → {destination.capitalize()}")
    print("─" * 45)
    print(f"📍 Distance(approx):      {round(distance, 2)} km")
    print(f"🚗 Transport:     {mode}")
    # print(f"💰 Currency:      {currency}")
    # print(f"🗣️  Language(s):   {', '.join(langlist)}")
    # print(f"📞 Calling code:  {', '.join(callingcode)}")
    print("─" * 45)
    print()
    