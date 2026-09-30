async def generate_recommendations(category, data):
    budget = data.get('budget', '50000')
    room_type = data.get('room_type', data.get('event_type', 'Bedroom'))
    quantity = data.get('quantity', data.get('guests', '1'))
    
    # Make sure budget is int
    try:
        b = int(budget)
    except:
        b = 50000

    if category == "home":
        return f"""
### 🏠 Budget Home Plan for {room_type} - Rs.{b}

**Your Budget: Rs.{b} for {room_type} x {quantity}**

**1. Furniture (60% - Rs.{int(b*0.6)}):**
- Bed/Cot - Rs.{int(b*0.3)}
- Wardrobe / Storage - Rs.{int(b*0.15)}
- Study Table & Chair - Rs.{int(b*0.15)}

**2. Decor & Lighting (20% - Rs.{int(b*0.2)}):**
- Wall Paint / Stickers - Rs.{int(b*0.1)}
- Lights & Lamps - Rs.{int(b*0.1)}

**3. Essentials (20% - Rs.{int(b*0.2)}):**
- Mattress, Curtains, etc - Rs.{int(b*0.2)}

**Shopping Tips:**
- Check IKEA, Pepperfry, Local Chennai shops in T.Nagar
- Buy during sale!

This plan is optimized for your budget!
"""
    else:
        return f"""
### 🎉 Party Plan for {room_type} - Rs.{b} - {quantity} Guests

**Budget Breakdown:**
- Food & Drinks (50%): Rs.{int(b*0.5)} - Rs.{int(b*0.5)//int(quantity) if quantity else 300} per person
- Decoration (20%): Rs.{int(b*0.2)}
- Venue/Sound (20%): Rs.{int(b*0.2)}
- Return Gifts (10%): Rs.{int(b*0.1)}

**Tips for {room_type} party!**
Plan ready da!
"""