import rdflib
import sqlalchemy

db = sqlalchemy.create_engine('postgresql://cthoyt:@localhost:5432/test')
print(db)

print(db.table_names())


graph = rdflib.Graph("cth_rdb2rdf_dm")
graph.open(db, base_iri="http://cthoyt.com/ns")

print(str(graph.serialize(format='turtle'), 'utf-8'))