def display_result(source,destination,distance,mode,currency,langlist,callingcode):
    print()
    print(f"✈️  TRIP SUMMARY: {source.title()} → {destination.title()}")
    print("─" * 45)
    print(f"📍 Distance(approx):  {round(distance, 2)} km" if distance is not None else "📍 Distance(approx):  Unknown")
    print(f"🚗 Transport(effcient):   {mode}")
    print(f"💰 Currency:      {','.join(currency)}")
    print(f"🗣️  Language(s):   {', '.join(langlist)}")
    print(f"📞 Calling code:  {','.join(callingcode)}")
    print("─" * 45)
    print()
    