# IITM Assignment API

This API automatically answers questions from graded assignments for the IIT Madras Online Degree in Data Science.

## Usage

Send a POST request to the `/api/` endpoint with:
- `question`: The assignment question
- `file` (optional): Any file attachment needed to answer the question

Example:
```bash
curl -X POST "http://localhost:8000/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the 'answer' column of the CSV file?" \
  -F "file=@abcd.zip"
```

Response:
```json
{
  "answer": "1234567890"
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
