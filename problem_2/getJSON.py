import json

def readTxt(filename):
    image_info = []
    with open(filename, 'r') as f:
        for line in f:
            #line for example is: 
            # 0 0.142857 0.439048 0.0942857 0.127619
            #split the line by white space
            line = line.split(' ')
            # extract x, y, width and height and removing the newline from height and parsing them into float
            image_info.append([float(line[1]), float(line[2]), float(line[3]), float(line[4].rstrip('\n'))])

    return image_info


filePath = 'problem2/image1.txt'
#calling function to read txt file
imgInfo = readTxt(filePath)
results = []

for line in imgInfo:
    imageRot = 0
    values = {
        "x": line[0],
        "y": line[1],
        "width": line[2],
        "height": line[3],
        "rotation": 0,
        "rectanglelabels": [
            "object"
        ]
    }    
    results.append({"image_rotation": imageRot,
                     "values" : values})

new_json = 'images.json'
ImgSpec = {"results": results}
main = json.dumps(ImgSpec, indent=4)
with open(new_json, "w") as j:
    j.write(main)    


#uncomment to get json like 'problem2/image1.json'
# main = {}
# main["annotations"] = [{"results": results}]
# main['data'] = {"image": "\/data\/upload\/image1.jpg"}
# main = json.dumps(main, indent=4)
# with open("imageSpecs.json", "w") as j:
#     j.write(main)    
