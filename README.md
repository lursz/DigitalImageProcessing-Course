# Digital Image Processing

## Table of contents
| Description   | Assignment & Solution | Homework  Assignment & Solution |
| ------------- | ------------- | ------------- |
| 01. Intro  |  [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)| [homework1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 02. Point transformations, LUT  |  [solution2](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab2)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 03. Histogram  |  [solution3](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab3)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 04. Thresholding  | [solution4](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab4)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 05. Resolution  |  [solution5](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab5)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 06. Context  |   [solution6](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab6)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 07. Bilateral  | [solution7](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab7)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 08. Fourier  |  [solution8](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab8)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 09. Canny  |  [solution9](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab9)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 10. Morphology  |  [solution10](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab10)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 11. Hough |  [solution11](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab11)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 12. Segmentation  |  [solution12](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab12)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|
| 13. Indexation  |  [solution13](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab13)| [solution1](https://github.com/lursz/DigitalImageProcessing-Course/tree/main/lab1)|

<details>
<summary>Some notes </summary>


## Transformations
Operacje arytmetyczne na pixelach:
- Dodawanie $f_3(x,y) = f_1(x,y) + f_2(x,y)$
- Odejmowanie $f_3(x,y) = f_1(x,y) - f_2(x,y)$
- Przemnożenie $f_3(x,y) = f_1(x,y) \cdot f_2(x,y)$
- Kombinacja liniowa (przenikanie) $f_3(x,y) = p \cdot f_1(x,y) + (1-p) \cdot f_2(x,y)$ p[0,1]
- Przemnożenie przez stałą $f_3(x,y) = f_1(x,y) \cdot k$
## Histogram
- Histogramem obrazu nazywamy wykres słupkowy zdefiniowany następującymi zależnościami:<br>
$$
\begin{equation}
h(i) = \sum_{x=0}^{N-1} \sum_{y=0}^{M-1} p(i,(x,y))
\end{equation}<br>
gdzie:<br>
\begin{equation}
p(i) =  \left\{
  \begin{array}{l l}
    1 & \quad \text{gdy} f(x,y) = i\\
    0 & \quad \text{gdy} f(x,y) \ne i
  \end{array} \right.
\end{equation}
$$

- Inaczej mówiąc, histogram zawiera informacje na temat tego ile pikseli o danym poziomie jasności występuje na obrazie (w przypadku obrazu w odcieniach szarości). Określa się to także rozkładem empirycznym cechy.

- Często wykorzystuje się tzw. znormalizowaną postać histogramu  – wszystkie wartości $h(i)$ są dzielone przez liczbę pikseli na obrazie.
Otrzymana w ten sposób wielkość to gęstość prawdopodobieństwa wystąpienia na obrazie pikseli o odcieniu $i$.

- Histogram można zdefiniować również dla obrazów kolorowych.
Otrzymujemy wtedy 3 histogramy – po jednym dla danej składowej: R,G,B (lub HSV, YCbCr, itp.) lub histogram trójwymiarowy.

- Histogram jest bardzo użyteczny w przetwarzaniu i analizie obrazów.
Wykorzystywany jest przy binaryzacji (szerzej na jednym z kolejnych laboratoriów) oraz do oceny jakości (dynamiki, kontrastu) obrazu.
W idealnym przypadku wszystkie poziomy jasności w obrazie powinny być wykorzystane (i to najlepiej w miarę jednolicie)  – obrazowo mówiąc histogram powinien rozciągać się od 0  – 255 (obraz w skali szarości).

- W przypadku gdy  wykorzystujemy jedynie fragment dostępnego zakresu (wąski histogram)  lub histogram nie jest jednolity (występują dominujące grupy pikseli) obraz ma dość słaby kontrast.
Cechę tę można poprawić stosując tzw. rozciąganie albo wyrównywanie histogramu (ang. *histogram equalization*).  
![](http://www.algorytm.org/images/stories/po/histogram.jpg)
## Binarization
Image processing technique used to convert a `grayscale image` into a `binary image`. 
`The binary image` consists of pixels that are either black or white, with no shades of gray in between. This process is often used in computer vision and image analysis tasks to simplify and highlight certain features in an image

Binarization formula:
$$
\begin{equation}
B(x, y) = 
\begin{cases}
1 & \text{if } I(x, y) \geq \text{threshold} \\
0 & \text{if } I(x, y) < \text{threshold}
\end{cases}
\end{equation}
$$

## Gamma modulation
Gamma modulation for photos is a technique used to adjust the brightness and contrast of digital images. It involves applying a non-linear correction to the pixel values, typically using a gamma curve, to match the way the human eye perceives light.

## Podział filtrów
- Filtry liniowe
- Filtry nieliniowe 

### Filtry liniowe
- `Convolution` is the process of transforming an image by applying a kernel over each pixel and its local neighbors across the entire image.  
![Convolution explained photo](https://miro.medium.com/v2/resize:fit:464/0*e-SMFTzO8r7skkpc)
- `Filtry dolnoprzepustowe` Filtry uśredniające, których maceirze konwolucji mogą przybrać następujące postacie, w zasadzie liczymy średnią artymetyczną lub ważona dla sąsiadujących pixeli:  
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/55db1801f327f9487c341ed9d2c2dec68678c932)

 Opiera się na usuwaniu dużych różnic w kolorach pomiędzy sąsiadującymi pikselami i przepuszczaniu elementów o niskiej częstotliwości (ogólnych kształtów, bez szczegółów). Filtry te przeważnie wykorzystuje się właśnie do eliminacji zakłóceń. Właściwie dopasowując rząd macierzy filtru można usuwać zakłócenia różnej wielkości, ograniczając przy tym utratę szczegółów(wysokich częstotliwości) w odfiltrowywanym obrazie. 

- `Filtry górnoprzepustowe` Filtry wydobywające szybkie zmiany jasności - kontury, krawędzie itd.  
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/fe38de3aec8305119766ff638d9e46a2e5e78cc3)  
 Popularnie mówi się że wyostrzajaa lub różniczkuja sygnał. Dzielimy na:
    - Lapsjany (wykrywające krawędzie)
    - Kierunkowe
    - Wykruwające narożniki

</details>