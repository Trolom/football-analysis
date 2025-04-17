from ultralytics import YOLO

model = YOLO('yolov8x.pt')

results = model.predict('08fd33_4.mp4', save=True)
print(results[0])

print('----------------------------------')
for box in results[0].boxes:
    print(box)

