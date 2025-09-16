import qrcode
import os
import random

# Danh sách link + tên vui
links = [
    ("https://www.youtube.com/watch?v=6n3pFFPSlW4", "You Been Trolled 😏"),
    ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Rickroll 🤣"),
    ("https://www.youtube.com/watch?v=j5a0jTc9S10", "Coffin Dance ⚰️"),
    ("https://www.youtube.com/watch?v=9Deg7VrpHbM", "Nyan Cat 🐱🌈"),
    ("https://www.youtube.com/watch?v=ZZ5LpwO-An4", "He-Man Song 💪🎤")
]

# Hỏi số lượng QR muốn tạo
try:
    total_qr = int(input("🔢 Bạn muốn tạo bao nhiêu QR code? "))
except ValueError:
    total_qr = 5
    print("⚠️ Nhập sai, mặc định tạo 5 QR code.")

# Tạo thư mục lưu QR nếu chưa có
output_folder = "qrcodes"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print(f"🎲 Đang tạo {total_qr} QR code (random từ {len(links)} link)...\n")

# Tạo QR code ngẫu nhiên
for i in range(1, total_qr + 1):
    chosen_link, name = random.choice(links)
    img = qrcode.make(chosen_link)
    file_name = os.path.join(output_folder, f"qrcode_random_{i}.png")
    img.save(file_name)
    print(f"✅ QR {i}: {name} -> {chosen_link}")

print("\n🎉 Hoàn tất! Các QR code đã được lưu trong thư mục 'qrcodes'.")

# Mở thư mục sau khi tạo xong
os.startfile(output_folder)
