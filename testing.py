from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(r'test videos\subway video.mp4', save=True)

print(results[0])
for box in results[0].boxes:
    print(box)




