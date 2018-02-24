from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add categories to db
category1 = Category(name="Foundation", image="/static/foundation.jpg")
session.add(category1)
session.commit()

category2 = Category(name="Concealer", image="/static/concealer.jpg")
session.add(category2)
session.commit()

category3 = Category(name="Blush", image="/static/blush.jpg")
session.add(category3)
session.commit()

category4 = Category(name="Eyeshadow", image="/static/eyeshadow.jpg")
session.add(category4)
session.commit()

category5 = Category(name="Lipstick", image="/static/lipstick.jpg")
session.add(category5)
session.commit()

category6 = Category(name="Bronzer", image="/static/bronzer.jpg")
session.add(category6)
session.commit()


# Add items to categories in db
item2 = Item(name="Vice Lipstick", brand="Urban Decay", description="An innovative lip formula, now in an array of shades and finishes - encased in a sleek, faceted case.",
             category=category5)
session.add(item2)
session.commit()

item3 = Item(name="Tarteist Quick Dry Matte Lip Paint", brand="Tarte", description="A quick-dry, full-coverage, transfer-proof liquid lipstick.",
             category=category5)
session.add(item3)
session.commit()

item4 = Item(name="Pro Filt'r Soft Matte Longwear Foundation", brand="Fenty Beauty", description="A soft matte, long-wear foundation with buildable, medium-to-full coverage, in a boundary-breaking range of shades.",
             category=category1)
session.add(item4)
session.commit()

item5 = Item(name="Lock It Foundation", brand="Kat Von D", description="A high-pigment, full-coverage foundation with a matte finish and 24-hour wear-now with a new look in a total of 30 shades.",
             category=category1)
session.add(item5)
session.commit()

item6 = Item(name="Natural Radiant Longwear Foundation", brand="NARS", description="A foundation with up to 16 hours of lightweight, natural, fade-resistant wear, featuring full-powered radiance to smooth the look of skin.",
             category=category1)
session.add(item6)
session.commit()

item7 = Item(name="All Hours Concealer", brand="Yves Saint Laurent", description="A new 16 hour-wear, full-coverage concealer that instantly and completel covers skin imperfections, yet does not crease, crack, or look masky.",
             category=category2)
session.add(item7)
session.commit()

item8 = Item(name="Amazonian Clay 12-Hour Blush", brand="Tarte", description="A long-wearing, solar-baked blush that lasts up to 12 hours.",
             category=category3)
session.add(item8)
session.commit()

item9 = Item(name="Ambient Lighting Blush Collection", brand="Hourglass", description="A groundbreaking hybrid that combines the customized lighting effects of Ambient Lighting Powder or Strobe Powder with a spectrum of breathtakingly modern hues.",
             category=category3)
session.add(item9)
session.commit()

item10 = Item(name="Modern Renaissance Palette", brand="Anastasia Beverly Hills", description="An essential eyeshadow collection with 14 shades in neutral to berry tones.",
              category=category4)
session.add(item10)
session.commit()

item11 = Item(name="Glitter & Glow Liquid Eye Shadow", brand="Stila", description="A brilliant and long-wearing, liquid glitter eyeshadow.",
              category=category4)
session.add(item11)
session.commit()

item12 = Item(name="Just Peachy Velvet Matte", brand="Too Faced", description="A long-wearing eyeshadow palette with 12 highly-pigmented, matte hues for endless eye looks.",
              category=category4)
session.add(item12)
session.commit()

print "Added categories and category items."
