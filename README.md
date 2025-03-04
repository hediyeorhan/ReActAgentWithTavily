# ReActAgentWithTavily

Bu çalışmada Google AI tarafından geliştirilen yapay zekâ Gemini API'ı kullanılarak temel bir ReAct Agent projesi geliştirilmiştir. 

Projede __.env__ dosyasında içeriğinde şu veriler bulunmaktadır.

• GEMINI_API_KEY=

• LANGCHAIN_API_KEY=

• LANGCHAIN_TRACING_V2=true

• LANGCHAIN_PROJECT=PROJECT_NAME

• TAVILY_API_KEY=

Projede, Gemini AI ile birlikte Langchain ve Langgraph framework'ü kullanılmıştır. Langchain, büyük dil modelleri ile uygulama geliştirilmesinde kullanılmaktadır. Zincir yapısında LLM'lerin birbirleri ile ve insanlar ile konuşmasını sağlamaktadır. Doküman okuma-yükleme, chat geçmişi tutma, embedding işlemleri ve vektör database işlemleri için langchain framework'ünden faydalanılmıştır. LangChain, LLM'ler ile entegrasyon sağlayarak özelleştirilmiş sorgu yönetimi sunmaktadır. Langgraph ise agent oluşturma, chat hafızasını bellekte / veri tabanında tutma gibi hizmetler sunmaktadır.

<h3> TAVILY </h3>

<br>
Bu çalışmada, Tavily kullanılarak LLM modelinin web sayfası araştırmaları ile entegre bir şekilde bir agent yapısında çalışması sağlanmıştır.


<br>

Langgraph kullanılarak chat hafızası bir veri tabanı dosyasına kayıt edilmiştir. Bu sayede eski chat konuşmaları kaybolmamıştır ve geliştirilen model daha tutarlı sonuçlar / cevaplar üretmiştir.

<h3> AGENT </h3>

<br>

Çalışmada kullanılan agent türü __reAct__'tır. Bu agent langgraph kullanılarak kod içerisinde oluşturulmuştur. Oluşturulan agent parametre olarak; api kullanılarak oluşturulan llm modelini, tavily search sonuçlarını ve Langchain hub üzerinden çekilen __hwchase17/react-chat__ prompt'unu almaktadır. __AgentExecutor__ metotu ise oluşturulan react agent, tavily search sonuçları ve chat hafızasını parametre olarak almaktadır. Aynı thread id içerisinde chat hafızası tutulmaktadır. Thread id değişirse chat hafızası sıfırlanmaktadır.

<br>

Çalışmada agent kendi içerisinde soru - cevap mekanizması çalıştırarak kullanıcının girdiği input'u nasıl değerlendireceğine karar vermektedir. Tool kullanmaya ihtiyacı var mı yok mu inputu değerlendirmektedir. Eğer tool kullanıldıysa oradan gelen cevapları da değerlendirerek bir cevap dönmektedir. Sonrasında kullanıcıya en uygun cevabı vermektedir.

Şekil 1'de başlangıç olarak geliştirilen asistan ile bir giriş konuşması yapılmıştır.
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/2d1abe47-6e9a-4411-aaa1-84a8cfe39fdd" alt="image">
</div>
Şekil 1. Başlangıç konuşması
<br>
<br>

Şekil 2'de bilgi almak istenilen konu belirtilmiştir. Burada agent tool kullanması gerektiğine karar vermiştir ve Tavily ile bir web search gerçekleştirmiştir. Sonuçları llm modeli ile değerlendirerek kullanıcıya mantıklı bir cevap dönmüştür.
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/c8c370d9-337c-4eb2-bb5c-051da8da53f2" alt="image">
</div>
Şekil 2. Agent tool kullanım örneği
<br>
<br>
 
Şekil 3 ve Şekil 4'te ise tool kullanımına gerek olmadığını düşünerek bir cevap verilmiştir.
<br>
<br>

<div align="center">
<img src="https://github.com/user-attachments/assets/1c9e1b2e-d6ea-4e20-9460-07f6d2fa870c" alt="image">
</div>
Şekil 3. Tool kullanımı olmadan bir örnek çıktı
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/1ba62592-623b-48ce-8770-2453963185bc" alt="image">
</div>
Şekil 4. Tool kullanımı olmadan bir örnek çıktı
<br>
<br>
Şekil 5'te ise konuşmanın son kısmı görülmektedir.
<br>
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/5b889207-049e-49ce-bb93-5ad9b9047248" alt="image">
</div>
Şekil 5. Konuşma sonu örnek çıktısı
<br>
<br>

