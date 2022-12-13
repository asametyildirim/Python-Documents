from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
# bağımsız değişkeni oluştur, bağımsız değişkenleri ayrıştır ve ayrıştır
""" 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())
"""
# define the answer key which maps the question number
# to the correct answer
# soru numarasını gösteren cevap anahtarını tanımlayın
# doğru cevaba
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

# load the image, convert it to grayscale, blur it
# görüntüyü yükleyin, gri tonlamaya dönüştürün, bulanıklaştırın
# slightly, then find edges
# hafifçe, sonra kenarları bulun
image = cv2.imread("test.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("blurred",blurred)
edged = cv2.Canny(blurred, 75, 200) #Kenar algılama
cv2.imshow("edged",edged)
# find contours in the edge map, then initialize
# the contour that corresponds to the document
# kenar haritasında konturları bulun, ardından başlatın
# belgeye karşılık gelen kontur
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE) #findContours 3 parametre alır. 1. si kaynak görüntü, 2. si kontur alma modu, 3. kontur alma yaklaşımı
#https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html
"""
cv2.RETR_LIST
Bu, dört bayrağın en basitidir (açıklama açısından). Basitçe tüm konturları alır, ancak herhangi bir ebeveyn-çocuk ilişkisi yaratmaz. Bu kurala göre ebeveynler ve çocuklar eşittir ve onlar sadece dış hatlardır . yani hepsi aynı hiyerarşi düzeyine aittir.
Yani burada hiyerarşi dizisindeki 3. ve 4. terim her zaman -1'dir. Ama açıkçası, Sonraki ve Önceki terimlerin karşılık gelen değerleri olacaktır. Sadece kendiniz kontrol edin ve onaylayın.
Aşağıda elde ettiğim sonuç var ve her satır karşılık gelen konturun hiyerarşi detayları. Örneğin, ilk satır kontur 0'a karşılık gelir. Sonraki kontur kontur 1'dir. Yani Sonraki = 1. Önceki kontur yoktur, dolayısıyla Önceki = -1. Ve kalan iki, daha önce de söylendiği gibi, -1'dir.
"""

"""
cv2.RETR_EXTERNAL
Bu bayrağı kullanırsanız, yalnızca aşırı dış bayrakları döndürür. Tüm çocuk konturları geride bırakılır. Bu yasaya göre, her ailede sadece en yaşlıya bakıldığını söyleyebiliriz. Ailenin diğer üyeleri umurlarında değil :) .
Öyleyse, görüntümüzde kaç tane aşırı dış kontur var? yani hiyerarşi-0 seviyesinde mi? Sadece 3, yani konturlar 0,1,2 değil mi? Şimdi bu bayrağı kullanarak konturları bulmaya çalışın. Burada da her elemana verilen değerler yukarıdaki ile aynıdır. Yukarıdaki sonuçla karşılaştırın. Aldıklarım aşağıda:
Yalnızca dış konturları çıkarmak istiyorsanız bu bayrağı kullanabilirsiniz. Bazı durumlarda yararlı olabilir.
"""

"""
cv2.RETR_CCOMP
Bu bayrak, tüm konturları alır ve onları 2 seviyeli bir hiyerarşiye göre düzenler. yani nesnenin dış konturları (yani sınırı) hiyerarşi-1'e yerleştirilir. Ve nesne içindeki deliklerin konturları (varsa) hiyerarşi-2'ye yerleştirilir. İçinde herhangi bir nesne varsa, konturu yine sadece hiyerarşi-1'e yerleştirilir. Ve hiyerarşi-2'deki boşluğu vb.
Sadece siyah bir arka plan üzerinde "büyük beyaz sıfır" görüntüsünü düşünün. Sıfırın dış çemberi birinci hiyerarşiye ve sıfırın iç çemberi ikinci hiyerarşiye aittir.
Bunu basit bir görselle açıklayabiliriz. Burada konturların sırasını kırmızı renkle, ait oldukları hiyerarşiyi yeşil renkle (1 veya 2) etiketledim. Sıra, OpenCV'nin konturları tespit ettiği sıra ile aynıdır.
İlk konturu düşünün, yani kontur-0. Hiyerarşi-1'dir. İki deliği vardır, konturlar 1 ve 2 ve hiyerarşi-2'ye aittirler. Yani kontur-0 için, aynı hiyerarşi seviyesindeki sonraki kontur kontur-3'tür. Ve bir önceki yok. İlki ise hiyerarşi-2'de kontur-1'dir. Hiyerarşi-1'de olduğu için ebeveyni yoktur. Yani hiyerarşi dizisi [3,-1,1,-1] şeklindedir.
Şimdi kontur-1'i alın. Hiyerarşi-2'dedir. Aynı hiyerarşide bir sonraki (kontur-1'in ebeveynliği altında) kontur-2'dir. Önceki yok. Çocuk yok ama ebeveyn kontur-0. Yani dizi [2,-1,-1,0] şeklindedir.
Benzer şekilde kontur-2 : Hiyerarşi-2'dedir. Kontur-0 altında aynı hiyerarşide bir sonraki kontur yoktur. Yani Sıradaki yok. Önceki, kontur-1'dir. Çocuk yok, ebeveyn kontur-0. Yani dizi [-1,1,-1,0].
Kontur - 3 : Hiyerarşi-1'de bir sonraki kontur-5'tir. Önceki, kontur-0'dır. Çocuk kontur-4'tür ve ebeveyni yoktur. Yani dizi [5,0,4,-1] şeklindedir.
Kontur - 4 : Kontur-3'ün altında hiyerarşi 2'de bulunur ve kardeşi yoktur. Yani sonraki yok, önceki yok, çocuk yok, ebeveyn kontur-3. Yani dizi [-1,-1,-1,3].
Kalanı doldurabilirsiniz. Aldığım son cevap bu:
"""
"""
4. RETR_TREE
Ve bu son adam, Mr.Perfect. Tüm konturları alır ve tam bir aile hiyerarşisi listesi oluşturur. Hatta dede, baba, oğul, torun ve hatta ötesinin kim olduğunu bile anlatır... :) .
Örneğin, yukarıdaki görüntüyü aldım, cv.RETR_TREE kodunu yeniden yazdım , konturları OpenCV tarafından verilen sonuca göre yeniden sıraladım ve analiz ettim. Yine kırmızı harfler kontur sayısını, yeşil harfler ise hiyerarşi düzenini verir.
Kontur-0 Al : Hiyerarşi-0'dadır. Aynı hiyerarşideki bir sonraki kontur, kontur-7'dir. Önceki kontur yok. Çocuk kontur-1'dir. Ve ebeveyn yok. Yani dizi [7,-1,1,-1] şeklindedir.
Al kontur-2 : Hiyerarşi-1'dedir. Aynı seviyede kontur yok. Önceki yok. Çocuk kontur-3'tür. Ebeveyn, kontur-1'dir. Yani dizi [-1,-1,3,1].
Ve kalan, kendini dene. Aşağıda tam cevap:
"""


"""
cv.CHAIN_APPROX_NONE öğesini geçerseniz , tüm sınır noktaları saklanır. Ama aslında tüm noktalara ihtiyacımız var mı? Örneğin, düz bir çizginin konturunu buldunuz. O çizgiyi temsil etmek için çizgideki tüm noktalara ihtiyacınız var mı? Hayır, o çizginin sadece iki uç noktasına ihtiyacımız var. 
cv.CHAIN_APPROX_SIMPLE bunu yapar. Tüm gereksiz noktaları kaldırır ve konturu sıkıştırarak hafızadan tasarruf sağlar.
Aşağıdaki dikdörtgen görüntüsü bu tekniği göstermektedir. Sadece kontur dizisindeki (mavi renkle çizilmiş) tüm koordinatların üzerine bir daire çizin. 
İlk resim cv.CHAIN_APPROX_NONE ile aldığım puanları (734 puan), ikinci resim cv.CHAIN_APPROX_SIMPLE ile aldığım puanları (sadece 4 puan) gösteriyor. Bakın, ne kadar bellek tasarrufu sağlıyor!!!
"""
cnts = imutils.grab_contours(cnts)
docCnt = None

# ensure that at least one contour was found
# en az bir kontur bulunduğundan emin olun
if len(cnts) > 0:
	# sort the contours according to their size in
	# descending order
	# konturları boyutlarına göre sırala
	# azalan sipariş
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

	# loop over the sorted contours
	# sıralanmış konturlar üzerinde döngü
	for c in cnts:
		# approximate the contour
		# kontura yaklaş
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)

		# if our approximated contour has four points,
		# then we can assume we have found the paper
		# eğer yaklaşık konturumuz dört noktaya sahipse,
		# o zaman kağıdı bulduğumuzu varsayabiliriz
		if len(approx) == 4:
			docCnt = approx


			print(docCnt)
			break

# apply a four point perspective transform to both the
# original image and grayscale image to obtain a top-down
# birds eye view of the paper
# her ikisine de dört noktalı bir perspektif dönüşümü uygulayın
# yukarıdan aşağıya elde etmek için orijinal görüntü ve gri tonlamalı görüntü
# kağıdın kuş bakışı görünümü
paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))

# apply Otsu's thresholding method to binarize the warped
# piece of paper
# çarpık olanı ikili hale getirmek için Otsu'nun eşikleme yöntemini uygulayın
# kağıt parçası
thresh = cv2.threshold(warped, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# find contours in the thresholded image, then initialize
# the list of contours that correspond to questions
# eşikli görüntüde konturları bulun, ardından başlatın
# sorulara karşılık gelen konturların listesi
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []
#cv2.rectangle(image, (248,304), (203,303), (0, 0, 255), 5)

# loop over the contours
i=1
for c in cnts:
	# compute the bounding box of the contour, then use the
	# bounding box to derive the aspect ratio
	# konturun sınırlayıcı kutusunu hesaplayın, ardından
	# en boy oranını elde etmek için sınırlayıcı kutu
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)

	# in order to label the contour as a question, region
	# should be sufficiently wide, sufficiently tall, and
	# have an aspect ratio approximately equal to 1
	# konturu bir soru, bölge olarak etiketlemek için
	# yeterince geniş, yeterince uzun ve
	# yaklaşık olarak 1'e eşit bir en boy oranına sahip
	if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
		questionCnts.append(c)
		i = i + 1
		if i == 2:
		    cv2.drawContours(image, c, -1, (0, 0, 255), 3)
		else:
			cv2.drawContours(image, c, -1, (0,255,0), 3)


# sort the question contours top-to-bottom, then initialize
# the total number of correct answers
questionCnts = contours.sort_contours(questionCnts,
	method="top-to-bottom")[0]
correct = 0
cv2.drawContours(image, questionCnts[1], -1, (255, 0, 255), 3)

# each question has 5 possible answers, to loop over the
# question in batches of 5
# her sorunun 5 olası yanıtı vardır,
#5'li gruplar halinde # soru
for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
	# sort the contours for the current question from
	# left to right, then initialize the index of the
	# bubbled answer
	# şu anki soru için konturları sırala
	# soldan sağa, ardından dizinin dizinini başlat
	# kabarcıklı cevap
	cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
	bubbled = None

	# loop over the sorted contours
	for (j, c) in enumerate(cnts):
		# construct a mask that reveals only the current
		# "bubble" for the question
		# sadece akımı gösteren bir maske oluşturun
		# soru için "kabarcık"
		mask = np.zeros(thresh.shape, dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)

		# apply the mask to the thresholded image, then
		# count the number of non-zero pixels in the
		# bubble area
		# maskeyi eşikli görüntüye uygulayın, ardından
		# sıfır olmayan piksel sayısını say
		# kabarcık alanı
		mask = cv2.bitwise_and(thresh, thresh, mask=mask)
		total = cv2.countNonZero(mask)

		# if the current total has a larger number of total
		# non-zero pixels, then we are examining the currently
		# bubbled-in answer
		# mevcut toplam daha büyük bir toplam sayısına sahipse
		# sıfır olmayan piksel, o zaman şu anda inceliyoruz
		# kabarcıklı cevap
		if bubbled is None or total > bubbled[0]:
			bubbled = (total, j)

	# initialize the contour color and the index of the
	# *correct* answer
	color = (0, 0, 255)
	k = ANSWER_KEY[q]

	# check to see if the bubbled answer is correct
	if k == bubbled[1]:
		color = (0, 255, 0)
		correct += 1

	# draw the outline of the correct answer on the test
	cv2.drawContours(paper, [cnts[k]], -1, color, 3)

# grab the test taker
score = (correct / 5.0)
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper, "{:.2f}".format(score), (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", paper)
cv2.waitKey(0)