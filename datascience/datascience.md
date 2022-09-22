## VERİ BİLİMİNİN GİRİŞ KAPISI

Teknoloji çağında yaşıyorken verilerin bize her an büyük bir yığın gibi görünmesi kaçınılmaz diyebiliriz. Peki verilerin her an her yerde karşımıza çıktığı bu dönemde veri biliminin rolü ne? Çoğu şirket, kurum ve kuruluş verilerden oluşan bir hazine sandığına sahip fakat bu sandık karışmasın diye bize bir düzenleyici gerekmez mi? İşte tam da bu noktada veri bilimi devreye giriyor. Veri bilimi makine öğrenmesi ve yapay zeka birbiri ile alakalı terimlerken ve herkesin bu kelimeleri sık sık kullanıp anlamını bilmemeleri üzerine size biraz bahsetmek istedim. Bu yazıma bu terimleri öğrenerek başlayabiliriz bence. Daha sonra

Yapay zekâ bilgisayarın insan davranışını bir biçimde taklit etmesini sağlamak anlamına gelir.
Veri bilimi, yapay zekanın bir alt kümesidir. Daha çok istatistik, bilimsel yöntemler ve veri analizinin örtüşen alanlarını ifade eder. Bunların tümü verilerden anlam çıkarmak ve iç görü elde etmek için kullanılır.
Makine öğrenimi, yapay zekanın bir diğer alt kümesidir. Bilgisayarların verilerden bir şeyler anlamasını ve yapay zeka uygulama yazılımları sunmayı sağlayan tekniklerden oluşur.
Ve yararlı bulduğumuz başka bir tanım ekleyelim.
Derin öğrenme, makine öğreniminin bir alt kümesidir ve bilgisayarların daha karmaşık sorunları çözmesini sağlar.
(https://www.oracle.com/tr/what-is-data-science/)

Bu terimleri öğrendikten sonra birlikte veri bilimine nerden başlanır ve nasıl bir yol izlenir sorularına yanıt olan ifade edilmiş CRISP-DM yönteminden bahsedelim.

CRISP-DM yöntemi bir veri bilimi projesine nereden başlanacağı, nasıl yönetileceği, hangi adımların izlenmesi gerektiği, projenin aşamalarının çıktıları ve
proje süresince ölçülebilir adımları değerlendiren bir yöntemdir.

CRISP-DM sürecinin aşamalarını inceleyelim:

İş anlayışı
Veriyi anlamayı
Verinin hazırlanması
Modelleme
Başarısının değerlendirmesi
Kullanıma sokulması
1.İş Anlayışı: İş probleminin, ele alıp çözülmek üzere veri bilimi takımına gelmiş olmasıdır. Örneğin, kullanıcılar araçlarını satmak istiyor ve buna uygun fiyat belirleme işlemi yapacaklar. Ama piyasayı sürekli takip edemedikleri için, yapay zekâ ile gerçekleştirilmiş bir programa ihtiyaçları vardır. “Kazası var mı, Araçta boya mevcut mu, Çizik var mı?” gibi birçok soru sorularak bir veri seti oluşturulur. Öncelikle model oluşturmak, bizim ana amacımız olarak görülür. Bu model;

Y = x1*b1 + x2*b2 + … + xp*bp

yani fonksiyon gibi düşünülecek ve bilinmeyen yerlere özellikler yazılıp nihai çözüme gidilecektir.

2.Veriyi Anlamak: Veri kaynaklarında veriler vardır ve bunlar veritabanı ortamları olarak geçer. Veri, basit bir excel tablosuna benzeyen özelliklerin olduğu setlerdir.

Veri kaynaklarından veriyi aldığımızda, veriyi anlayıp incelememiz gerekir. Ortalama, standart sapma, özetle istatistiksel sonuçlar çıkarmamız gerekir. Veriyi anlayacağımız hale getirmek için işlemler gerçekleştirmeliyiz. Verinin yapısını öğrendikten sonra verinin hazırlanması basamağına geçeriz.

3.Verinin Hazırlanması: Modelleme çalışmasına geçmeden önce veri setini hazırlamamız gerekir. Veri setindeki yapısal bozuklukları ve hazırlanması gereken yerleri düzenlememiz gerekmektedir. Düzenlenmesi gereken veriler;

Missing value: Kaybolmuş değer anlamına gelir, eksik veridir.
Aykırı değer: Verinin yapısının oldukça dışında kalan değerlere denir.
Gürültü: Bozuk değer anlamına gelir.
Bu aşamada verinin bozukluğu giderilir.

4.Modelleme: Veri içerisinde yer alan yapıların algoritmalara, fonksiyonlara öğretilmesi olayıdır. Arabanın özelliklerini girdiğimizde fiyatını verecek dediğimiz şey fonksiyondan ibaret olacaktır. Veri setinin içindeki yapıların öğrenilmesi gereken özelliklerini, katkılarını ve etkilerini bulmamız gerekir. Bu sebeple çoklu doğrusal regresyon modeli önemlidir. Veri setine çoklu doğrusal regresyon modelini verip aralarında ki ilişkiyi modellediğimizde;

Y = x1*b1 + x2*b2 + … + xp*bp

fonksiyonunu bulmaya çalıştığımızı biliyoruz.

Y: tahmin fonksiyonu

X değişkenleri: veri setinin içinden öğrenecek olduğumuz değişkenlerin etki düzeylerini ve yönlerini belirtecek olan katsayılardır. Yönünü ve şiddetini etkileyecek katsayıları ortaya çıkarır.

5.Değerlendirme (Model başarı değerlendirme): Kurulan modelin başarısının ve doğruluğunun değerlendirilmesi gerekir. Makine öğrenmesi modeli kurup değerlendirme işlemini ele alalım. Değerlendirme derken performans ele alınır.

Modele, çıktısının ne olduğunu bildiğimiz değerler verilir ve tahmini olarak ne değer vereceği, gerçek değer ile modelin tahmin ettiği değer karşılaştırılır. Başarısı değerlendirilir. Gerçek değerler ile tahmin edilen değerler arasındaki farkları minimum seviyeye indirgemek için farklı algoritmalar denenebilir.

6. Kullanıma Sokma: Nihai olarak karar verilen şekliyle, canlı sistemlere entegrasyon yapılır. Bu excel tablosu, veri tabanı tablosu sekliyle ya da rapor şeklinde kullanıma sokulabilir. Bir web sitesine de entegre edilebilir.

(https://www.veribilimiokulu.com/veri-bilimi-ve-yapay-zeka-nedir/)

İşte birlikte veri bilimi projesi aşamalarını incelemiş olduk. Bunlara uymaya çalışarak veri biliminin giriş kapısının anahtarını saksının altına bakıp kolayca bulabileceğimize inanıyorum:)







