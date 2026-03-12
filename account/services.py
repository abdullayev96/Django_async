# from .models import User
# from profiles.models import UserProfile
#
#
#
# async def upgrade_to_premium(user_id):
#     # Foydalanuvchini bazadan topamiz
#     user = await User.objects.aget(id=user_id)
#     profile = await UserProfile.objects.aget(user=user)
#
#     # 1. Balansni tekshiramiz (masalan, Premium obuna 50,000 so'm)
#     subscription_price = 50000
#     if profile.balance >= subscription_price:
#         # 2. Pulni yechamiz
#         profile.balance -= subscription_price
#         await profile.asave()
#
#         # 3. Statusni o'zgartiramiz
#         user.is_premium = True
#         await user.asave()
#
#         return {"status": "success", "message": "Tabriklaymiz! Siz Premium statusiga ega bo'ldingiz."}
#
#     return {"status": "error", "message": "Mablag' yetarli emas."}