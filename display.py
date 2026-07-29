def display_result(source,destination,mode,currency,langlist,callingcode):
    print()
    print(f"✈️  TRIP SUMMARY: {source.capitalize()} → {destination.capitalize()}")
    print("─" * 45)
    print(f"🚗 Transport:     {mode}")
    print(f"💰 Currency:      {currency}")
    print(f"🗣️  Language(s):   {', '.join(langlist)}")
    print(f"📞 Calling code:  {callingcode}")
    print("─" * 45)
    print()
    