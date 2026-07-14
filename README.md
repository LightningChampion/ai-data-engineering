# ai-data-engineering
Four-week preparation focused on Python, SQL, PySpark, Microsoft Fabric, Google Cloud, BigQuery and RAG.



# Gün 14 — Microsoft Fabric Tanışma

Bugün öğrendiklerim:

- Workspace oluşturma
- Lakehouse oluşturma
- Lakehouse içinde Files ve Tables farkı
- CSV dosyasını Lakehouse'a yükleme
- CSV dosyasını tabloya çevirme
- SQL analytics endpoint kullanma
- SQL ile Lakehouse tablosunu sorgulama
- Notebook oluşturma
- Notebook'a Lakehouse bağlama
- PySpark ile Lakehouse tablosu okuma
- Yeni sütun oluşturma
- groupBy ile kategori bazlı analiz yapma
- Analiz sonucunu Lakehouse'a yeni tablo olarak kaydetme

Önemli kavramlar:

- Workspace = proje çalışma alanı
- Lakehouse = veri deposu
- Files = ham dosyalar
- Tables = sorgulanabilir tablolar
- SQL analytics endpoint = Lakehouse tablolarını SQL ile sorgulama alanı
- Notebook = PySpark / Python ile veri işleme alanı

Bugünkü akış:

CSV → Lakehouse Files → Table → SQL sorgusu → Notebook → PySpark analiz → Yeni tablo

Oluşturulan tablolar:

- sales_data
- category_revenue







# Gün 15 — Fabric Lakehouse Mini Pipeline

Bugün Microsoft Fabric içinde küçük bir Lakehouse pipeline yaptım.

Akış:

CSV / sales_data tablosu
→ Notebook ile okuma
→ PySpark ile veri kontrolü
→ total_revenue sütunu oluşturma
→ prepared_sales_data tablosu olarak kaydetme
→ city_revenue analizi oluşturma
→ category_revenue analizi oluşturma
→ SQL analytics endpoint üzerinden sorgulama

Öğrendiğim kavramlar:

- Lakehouse içinde tablo okuma:
  `spark.read.table("sales_data")`

- Veri tiplerini kontrol etme:
  `df.printSchema()`

- NULL kontrolü:
  `col(c).isNull()`

- Yeni sütun oluşturma:
  `withColumn("total_revenue", col("quantity") * col("price"))`

- Analiz tablosu oluşturma:
  `groupBy().agg()`

- Lakehouse’a tablo kaydetme:
  `saveAsTable()`

- SQL endpoint üzerinden sorgulama:
  `SELECT * FROM dbo.city_revenue;`

Oluşturulan tablolar:

- sales_data
- prepared_sales_data
- city_revenue
- category_revenue

Kısa özet:

Bugün Fabric içinde veriyi Lakehouse’dan okuyup Notebook ile işledim. PySpark ile analiz tabloları oluşturdum ve sonuçları tekrar Lakehouse’a Delta table olarak kaydettim. Daha sonra SQL analytics endpoint ile bu tabloları sorguladım.




GÜN -16



# Fabric PySpark Lakehouse Project

This project is a basic data pipeline built with Microsoft Fabric Lakehouse and PySpark.

## Project Goal

The goal of this project is to create a simple end-to-end data pipeline:

CSV / Lakehouse table  
→ PySpark Notebook  
→ Prepared sales table  
→ Revenue analysis tables  
→ SQL analytics endpoint queries

## Tools Used

- Microsoft Fabric
- Lakehouse
- Notebook
- PySpark
- SQL analytics endpoint
- Delta Tables

## Dataset

The dataset contains simple sales data.

Main columns:

- order_id
- customer
- city
- category
- product
- quantity
- price
- order_date

## Pipeline Steps

### 1. Load sales data

The original sales data was uploaded into Microsoft Fabric Lakehouse as a table named:

```text
sales_data




# Gün 17 — Google Cloud Intro

Bugün Google Cloud ortamını tanıdım.

## Yapılanlar

- Google Cloud Console'a giriş yapıldı
- MFA / 2-step verification aktif edildi
- Yeni Google Cloud Project oluşturuldu
- Billing account mantığı öğrenildi
- IAM ekranı incelendi
- Service Accounts ekranı incelendi
- Cloud Storage ekranı açıldı
- BigQuery Studio açıldı
- Basit test SQL sorgusu çalıştırıldı

## Project

Kullanılan project:

```text
gcp-data-practice



day -18

# Day 18 - BigQuery Basic SQL

Today I practiced basic SQL queries in Google BigQuery using a public dataset.

## Dataset

`bigquery-public-data.samples.shakespeare`

## Topics Practiced

- SELECT
- FROM
- WHERE
- ORDER BY
- LIMIT
- COUNT
- SUM
- AVG
- GROUP BY
- HAVING
- DISTINCT
- LIKE
- IN
- BETWEEN
- AND / OR
- CASE WHEN

## Example Query

```sql
SELECT 
  word,
  SUM(word_count) AS total_count
FROM `bigquery-public-data.samples.shakespeare`
GROUP BY word
HAVING total_count > 500
ORDER BY total_count DESC
LIMIT 20;






# Day 19 - BigQuery Intermediate SQL

Today I practiced intermediate SQL concepts in Google BigQuery.

## Topics Practiced

- INNER JOIN
- LEFT JOIN
- Table aliases
- COALESCE
- CTE
- Window functions
- ROW_NUMBER
- RANK
- DENSE_RANK
- QUALIFY
- LAG
- LEAD
- Running total
- Partitioning and clustering concepts

## JOIN

JOIN is used to combine two tables using a common column.

Example:

```sql
SELECT 
  c.customer_name,
  o.order_id,
  o.amount
FROM customers AS c
JOIN orders AS o
  ON c.customer_id = o.customer_id;





# Day 20 - Cloud Storage to BigQuery Flow

Today I practiced loading a CSV file from local computer to Google Cloud Storage and then creating a BigQuery table from that file.

## Goal

The goal of this day was to understand the basic data loading flow:

Local CSV file → Cloud Storage Bucket → BigQuery Table → SQL Analysis

## Steps Completed

1. Created a CSV file.
2. Created a Cloud Storage bucket.
3. Uploaded the CSV file to the bucket.
4. Created a BigQuery dataset.
5. Created a BigQuery table from the CSV file.
6. Queried the table using SQL.
7. Calculated total revenue by category.

## Cloud Storage

I created a Cloud Storage bucket and uploaded the CSV file.

Bucket:

```text
gcp-data-practice-day20-bucket




# Day 22 - Embedding Introduction

Today I learned the basic idea of embeddings, vectors, cosine similarity, and semantic search.

## Topics Practiced

- Embedding
- Vector
- Cosine similarity
- Semantic similarity
- Semantic search
- SentenceTransformer
- Finding the most relevant sentence for a query

## What is an Embedding?

An embedding is a numerical representation of text.

A sentence is converted into a vector, which is a list of numbers.

Example:

```text
"I like playing football." → [0.12, -0.44, 0.08, ...]




# Day 23 - ChromaDB Similarity Search

Today I practiced storing documents in ChromaDB and searching for semantically similar documents.

## Topics Practiced

- ChromaDB client
- Collection
- Documents
- IDs
- Metadata
- Similarity search
- Metadata filtering
- Distance scores
- Top 3 search results

## Create a Collection

```python
import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="technology_documents"
)






Manual RAG — Chunk ve Chunk Overlap
Bugün öğrendiklerim:
* Metni cümlelere ayırma
* Cümleleri chunk’lara bölme
* Chunk size mantığı
* Chunk overlap mantığı
* Bir cümlenin birden fazla chunk içinde bulunması
* Overlap kullanarak bilgi kaybını azaltma
* Chunk’ları ChromaDB collection içine ekleme
* ChromaDB ile benzerlik araması yapma
* n_results ile getirilecek sonuç sayısını belirleme
* Retriever’ın soruya en yakın chunk’ları seçme mantığı
Önemli kavramlar:
* Chunk = uzun metnin küçük parçalara ayrılmış hâli
* Chunk size = bir chunk içinde bulunacak içerik miktarı
* Chunk overlap = önceki chunk’taki bazı bilgilerin sonraki chunk’ta tekrar kullanılması
* Collection = ChromaDB içinde document ve embedding’lerin tutulduğu alan
* Retrieval = soruya en yakın bilgilerin bulunması
* Retriever = en uygun chunk’ları seçen yapı
* Distance = soru ile chunk arasındaki benzerlik uzaklığı
* n_results = arama sonucunda döndürülecek chunk sayısı
Bugünkü akış:
Cümle listesi → Chunk oluşturma → Overlap ekleme → ChromaDB collection → Document ekleme → Soru gönderme → En yakın chunk’ları bulma
Oluşturulan yapılar:
* sentences
* overlap_chunks
* overlap_collection
* result
Overlap örneği:
Python + Pandas
Pandas + PySpark
PySpark + BigQuery
BigQuery + Cloud Storage
Burada her yeni chunk, önceki chunk’tan bir cümleyi tekrar kullanır. Böylece bağlantılı bilgiler chunk sınırında kaybolmaz.













# Gün 26 — LangChain ile RAG

Bugün öğrendiklerim:

- LangChain'in temel yapısı
- TextLoader ile TXT dosyası okuma
- PyPDFLoader ile PDF dosyası okuma
- RecursiveCharacterTextSplitter ile otomatik chunk oluşturma
- HuggingFace Embedding modeli kullanma
- Chroma Vector Store oluşturma
- Retriever oluşturma
- Retriever ile en yakın chunk'ları bulma
- Context oluşturma
- Prompt hazırlama
- FLAN-T5 modeli ile context kullanarak cevap üretme
- Aynı RAG yapısını TXT ve PDF dosyalarında uygulama

Önemli kavramlar:

- LangChain = LLM uygulamalarını geliştirmeyi kolaylaştıran framework
- Document Loader = Dosyaları okuyup Document nesnesine dönüştürür
- Text Splitter = Document'ları otomatik olarak chunk'lara ayırır
- Embedding Model = Metni sayısal vektörlere dönüştürür
- Vector Store = Embedding'leri saklayan veritabanı
- Chroma = LangChain ile kullanılan vector database
- Retriever = Soruya en uygun chunk'ları seçer
- Context = LLM'e gönderilecek ilgili bilgiler
- Prompt = LLM'e verilen son talimat

Bugünkü akış:

TXT / PDF → Document Loader → Text Splitter → Embedding Model → Chroma Vector Store → Retriever → Context → Prompt → FLAN-T5 → Cevap

Oluşturulan yapılar:

- company_info.txt
- company_report.pdf
- documents
- pdf_chunks
- embeddings
- vectorstore
- pdf_vectorstore
- retriever
- pdf_retriever
- context
- prompt

Manual RAG vs LangChain:

Manual RAG:
- Chunk oluşturma
- Embedding oluşturma
- ChromaDB ekleme
- Retrieval işlemleri
- Prompt hazırlama

LangChain:
- Aynı işlemleri hazır bileşenlerle otomatik gerçekleştirir.






# Gün 27 — Kurumsal Veri + RAG

Bugün öğrendiklerim:

- Pandas ile satış verisi oluşturma
- groupBy kullanarak kategori bazında gelir analizi yapma
- Analiz sonucunu doğal dile dönüştürme
- HuggingFace Embedding modeli oluşturma
- Analiz metnini Chroma Vector Store'a ekleme
- Retriever oluşturma
- Retriever ile en ilgili bilgiyi bulma
- Context hazırlama
- Prompt oluşturma
- FLAN-T5 modeli ile context kullanarak cevap üretme
- Kurumsal veri üzerinde uçtan uca RAG akışını uygulama

Önemli kavramlar:

- Structured Data = Tablo biçimindeki veriler
- Summary Text = Analiz sonucunun doğal dile çevrilmiş hâli
- Embedding = Metnin sayısal vektör gösterimi
- Vector Store = Embedding'leri saklayan veritabanı
- Retriever = En alakalı bilgiyi bulan yapı
- Context = LLM'e gönderilecek ilgili bilgiler
- Prompt = LLM'e verilen son talimat
- Generation = Context kullanılarak cevabın üretilmesi

Bugünkü akış:

CSV / Tablo
→ Pandas Analizi
→ Summary Text
→ Embedding
→ Chroma Vector Store
→ Retriever
→ Context
→ Prompt
→ FLAN-T5
→ Cevap

Oluşturulan yapılar:

- sales
- summary
- text
- embeddings
- company_db
- retriever
- results
- context
- prompt
- tokenizer
- model
- answer

Gerçek şirket kullanım alanları:

- Satış raporlarını sorgulama
- Finansal özetlerden soru-cevap
- ERP ve CRM verileri üzerinde kurumsal asistan
- İnsan kaynakları dokümanlarında arama
- Bilgi bankası ve iç doküman chatbotları
- Yönetim raporlarından otomatik bilgi çıkarma




