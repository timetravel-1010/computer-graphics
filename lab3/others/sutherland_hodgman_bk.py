def sutherlandHodgmanClip(subjectPolygon, clipPolygon): #poligono, viewport
   def inside(p):
      return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])
 
   def computeIntersection():
      dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
      dp = [ s[0] - e[0], s[1] - e[1] ]
      n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
      n2 = s[0] * e[1] - s[1] * e[0] 
      n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
      return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]
 
   outputList = subjectPolygon
   cp1 = clipPolygon[-1]
 
   for clipVertex in clipPolygon:
      cp2 = clipVertex
      inputList = outputList
      outputList = []
      print("inputList: ", inputList)
      s = inputList[-1]
 
      for subjectVertex in inputList:
         e = subjectVertex
         if inside(e):
            if not inside(s):
               outputList.append(computeIntersection())
            outputList.append(e)
         elif inside(s):
            outputList.append(computeIntersection())
         s = e
      cp1 = cp2
   return(list(map(lambda x: list(map(lambda y: int(y), x)), outputList)))

if __name__ == '__main__':
   # sutherlandHodgman(poligono, viewport)
   #nuevos_puntos = sutherlandHodgmanClip([[100,290],[100,210],[275,230],[150,250],[275,270],[100,290]], [[200, 200], [400, 200], [400, 300], [200, 300]])
   nuevos_puntos = sutherlandHodgmanClip([[20,20],[5,10],[7,12],[22,10],[25,10]], [[100, 100], [400, 200], [400, 300], [200, 300]])
   #print("nuevos puntos: ", nuevos_puntos)
   #puntos = list(map(lambda x: list(map(lambda y: int(y), x)), nuevos_puntos))
   print("puntos: ", nuevos_puntos)