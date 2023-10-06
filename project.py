import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_description = docx2txt.process("jobdescription.docx")

cv1 = docx2txt.process("cv1.docx")
cv2 = docx2txt.process("cv2.docx")

content1 = [job_description,cv1]

thecv = CountVectorizer()

matrix1 = thecv.fit_transform(content1)
similarity_matrix1 = cosine_similarity(matrix1)

content2 = [job_description,cv2]

matrix2 = thecv.fit_transform(content2)
similarity_matrix2 = cosine_similarity(matrix2)

#calculates the similarity score as decimals
res1 = similarity_matrix1[0][1]
res2 = similarity_matrix2[0][1]

def results(res1,res2):
    if res1> res2:
        print("the first cv matches the description better")
    else:
        print("the second cv matches the job description better")

results(res1,res2)


