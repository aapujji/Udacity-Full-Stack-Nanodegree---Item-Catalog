from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Aanandita", email="aapujji@gmail.com")
session.add(User1)
session.commit()

# Add categories to db
category1 = Category(user_id=1, name="Foundation",
                     image="/static/foundation.jpg")
session.add(category1)
session.commit()

category2 = Category(user_id=1, name="Concealer",
                     image="/static/concealer.jpg")
session.add(category2)
session.commit()

category3 = Category(user_id=1, name="Blush",
                     image="/static/blush.jpg")
session.add(category3)
session.commit()

category4 = Category(user_id=1, name="Eyeshadow",
                     image="/static/eyeshadow.jpg")
session.add(category4)
session.commit()

category5 = Category(user_id=1, name="Lipstick",
                     image="/static/lipstick.jpg")
session.add(category5)
session.commit()

category6 = Category(user_id=1, name="Bronzer",
                     image="/static/bronzer.jpg")
session.add(category6)
session.commit()


# Add items to categories in db
item1 = Item(name="Vice Lipstick", brand="Urban Decay",
             description="An innovative lip formula, "
             "now in an array of shades and finishes - "
             "encased in a sleek, faceted case.",
             image="/static/urban_decay_vice_lipstick.jpg",
             category=category5, user_id=1)
session.add(item1)
session.commit()

item2 = Item(name="Tarteist Quick Dry Matte Lip Paint", brand="Tarte",
             description="A quick-dry, full-coverage, "
             "transfer-proof liquid lipstick.",
             image="/static/tarte_quick_dry_lip_paint.jpg",
             category=category5, user_id=1)
session.add(item2)
session.commit()

item3 = Item(name="Pro Filt'r Soft Matte Longwear Foundation",
             brand="Fenty Beauty",
             description="A soft matte, long-wear foundation "
             "with buildable, medium-to-full coverage, "
             "in a boundary-breaking range of shades.",
             image="/static/fenty_beauty_pro_filtr.jpg",
             category=category1, user_id=1)
session.add(item3)
session.commit()

item4 = Item(name="Lock It Foundation", brand="Kat Von D",
             description="A high-pigment, full-coverage foundation "
             "with a matte finish and 24-hour wear - "
             "now with a new look in a total of 30 shades.",
             image="/static/kat_von_d_lock_it.jpg",
             category=category1, user_id=1)
session.add(item4)
session.commit()

item5 = Item(name="Natural Radiant Longwear Foundation", brand="NARS",
             description="A foundation with up to 16 hours of lightweight, "
             "natural, fade-resistant wear, featuring full-powered "
             "radiance to smooth the look of skin.",
             image="/static/nars_natural_radiant_longwear.jpg",
             category=category1, user_id=1)
session.add(item5)
session.commit()

item6 = Item(name="All Hours Concealer", brand="Yves Saint Laurent",
             description="A new 16 hour-wear, full-coverage concealer "
             "that instantly and completel covers skin imperfections, "
             "yet does not crease, crack, or look masky.",
             image="/static/yves_saint_laurent_all_hours.jpg",
             category=category2, user_id=1)
session.add(item6)
session.commit()

item7 = Item(name="Amazonian Clay 12-Hour Blush", brand="Tarte",
             description="A long-wearing, solar-baked blush "
             "that lasts up to 12 hours.",
             image="/static/tarte_amazonian_clay.jpg",
             category=category3, user_id=1)
session.add(item7)
session.commit()

item8 = Item(name="Ambient Lighting Blush Collection", brand="Hourglass",
             description="A groundbreaking hybrid that combines the "
             "customized lighting effects of Ambient Lighting Powder "
             "or Strobe Powder with a spectrum of breathtakingly modern hues.",
             image="/static/hourglass_ambient_lighting.jpg",
             category=category3, user_id=1)
session.add(item8)
session.commit()

item9 = Item(name="Modern Renaissance Palette",
             brand="Anastasia Beverly Hills",
             description="An essential eyeshadow collection "
             "with 14 shades in neutral to berry tones.",
             image="/static/anastasia_modern_renaissance.jpg",
             category=category4, user_id=1)
session.add(item9)
session.commit()

item10 = Item(name="Glitter & Glow Liquid Eye Shadow", brand="Stila",
              description="A brilliant and long-wearing, liquid glitter "
              "eyeshadow.",
              image="/static/stila_glitter_glow_liquid.jpg",
              category=category4, user_id=1)
session.add(item10)
session.commit()

item11 = Item(name="Just Peachy Velvet Matte", brand="Too Faced",
              description="A long-wearing eyeshadow palette "
              "with 12 highly-pigmented, matte hues for endless eye looks.",
              image="/static/too_faced_just_peachy_mattes.jpg",
              category=category4, user_id=1)
session.add(item11)
session.commit()

print "Added categories and category items."
