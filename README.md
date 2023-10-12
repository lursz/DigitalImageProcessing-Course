# Przetwarzanie obrazów cyfrowych
## Transformations
Operacje arytmetyczne na pixelach:
- Dodawanie $f_3(x,y) = f_1(x,y) + f_2(x,y)$
- Odejmowanie $f_3(x,y) = f_1(x,y) - f_2(x,y)$
- Przemnożenie $f_3(x,y) = f_1(x,y) \cdot f_2(x,y)$
- Kombinacja liniowa (przenikanie) $f_3(x,y) = p \cdot f_1(x,y) + (1-p) \cdot f_2(x,y)$ p[0,1]
- Przemnożenie przez stałą $f_3(x,y) = f_1(x,y) \cdot k$

## Histogram
Histogram to wykres słupkowy, którego wartości odzwierciedlają częstotliwość poszczególnych odcieni. Służy on do pomiaru jasności obrazu.  
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