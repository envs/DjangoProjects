var mlExtractions = {

	"schema": {
		"type": "array",
		    "items": {
		        "type": "object",
		        "properties": {
		            "modelName": {
		                "type":"string",
		                "title":"Extraction Model Name"
		            },                
		            "numberOfFields": {
		                "type": "number",
		                "default": 10,
		                "title": "Number of fields"
		            },
		            "numberOfDocs": {
		                "type": "number",
		                "default": 500,
		                "title": "Number of docs"
		            },
		            "numberOfPages": {
			            "type": "number",
			            "title": "Number of pages",
			            "enum": [1, 1.5, 2]
		        	},
		        	"documentFormat": {
			            "type": "number",
			            "title": "Document Format",
			            "enum": [1, 1.5]
		        	},
		        	"language": {
			            "type": "number",
			            "title": "Language",
			            "enum": [1, 1.5, 2]
		        	},
		        	"successCriteria": {
			            "type": "number",
			            "title": "Success Criteria",
			            "enum": [1, 2, 3]
		        	},
		        	"fieldsComplexity": {
		                "type": "string",
		                "default": "50/30/20",
		                "title": "Simple/Medium/Complex (%)"
		            }

		        }
		    }
		    
        },
	


	"options": {
		"type": "table",
		"items": {
		    "fields": {  
			    "numberOfPages": {
			        "type": "select",
			        "removeDefaultNone": true,
			        "default":1,
			        "optionLabels": ["1-5", "5-20", "20+"]
			    }, 
			    "documentFormat": {
			        "type": "select",
			        "removeDefaultNone": true,
			        "default":1,
			        "optionLabels": ["html, xml, pdf, image", "plain text (email body)"]
			    },      
			    "language": {
			        "type": "select",
			        "removeDefaultNone": true,
			        "default":1,
			        "optionLabels": ["English", "Other Western Languages", "Other languages (e.g. Asian)"]
			    },  
			    "successCriteria": {
			        "type": "select",
			        "removeDefaultNone": true,
			        "default":1,
			        "optionLabels": ["P:90% R:50%", "P:95% R:60%", "P:98% R:70%"]
			    },             						                
		       
		       
		    }
		}
	}
}