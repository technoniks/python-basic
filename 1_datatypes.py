students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}

print("=== Student Averages ===")
topper = None
avgAll = 0
for name, marks in students.items():
  sum = 0
  if topper is None:
    topper = name
  for mark in marks:
    sum += mark
  avg = sum / len(marks)
  avgAll += avg
  marks.append(avg)
  if students[topper][-2] < avg:
    topper = name
  if avg >= 80:
    marks.append("Topper")
  if avg >= 60 and avg < 80:
    marks.append("Pass")
  if avg < 60:
    marks.append("Needs improvement")
  print(f"{name}: {avg:.2f} - {marks[-1]}")
avgAll = avgAll / len(students.items())
print()
print("=== Class Topper ===")
print(f"{topper} with avarage {students[topper][-2]:.2f}")
print()
print("=== Class Average ===")
print(f"{avgAll:.2f}")
