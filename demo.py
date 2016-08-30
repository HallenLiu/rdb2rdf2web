
import psycopg2
import rdflib


db_string = 'postgresql://cthoyt:@localhost:5432/postgres'

xsd_types = {
	0: "xsd_string"
}


mapping = {
	"wk.documents": {
		"class": "http://cthoyt.com/ns/Document",
		"pkey": "document_id",
		"columns": {
			"doi":"",
			"title": 0
		}
	}



}


graph = rdflib.Graph()

conn = psycopg2.connect(db_string)

conn.close()
