from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()
with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='INR')
    bot.select_place_to_go(place_to_go='Digha')
    bot.select_date(checkin_date='2024-03-19', checkout_date="2024-03-21")
    bot.select_adault()