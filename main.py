from hanois import HanoiGame, HanoiTower, HanoiMovement
from location_circles_lab import DetectHanoiTower

if __name__ == "__main__":
    image_file = 'examples/imagen_20241205_143702.png'
    detect_hanoi = DetectHanoiTower()
    output,detection,_,_ = detect_hanoi.main(image_file)

    detect_hanoi.show_image(detection, 'Detection')

    output = output.tolist()

    game = HanoiGame(towers=3, discs=5,target_tower=2,start_tower=1,aux_tower=2,standard_start=False)
    game.towers.append(HanoiTower(discs=output[0]))
    game.towers.append(HanoiTower(discs=output[1]))
    game.towers.append(HanoiTower(discs=output[2]))

    game.paintHanoi()
    
    solutions = game.getRandomHanoiSolutionArray()

    sendToMaylen = []
    for sol in solutions:
        sendToMaylen.append(sol.getMatrix())

    print("Respuesta: ",sendToMaylen)