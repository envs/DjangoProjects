var mlClassifications = {

	"schema": {
		"title":"ASDASD",
		"type": "array",
		"items": {
		    "type": "object",
		    "properties": {
		        "modelName": {
		            "type":"string",
		            "title":"Classification Model Name"
		        },                
		        "numberOfClasses": {
		            "type": "number",
		            "title": "Number of classes",
		            "enum": [10, 20, 30, 50]
		        },
		        "type": {
		            "type": "string",
		            "title": "Type",
		            "enum": ["rule", "ml"]
		        }
		    }
		}
	},


	"options": {
		"label": "ASDASD",
		"type": "table",
		"items": {
		    "fields": {
		        "numberOfClasses": {
		            "type": "select",
		            "removeDefaultNone": true,
		            "default":10,
		            "optionLabels": ["1-10", "10-20", "20-30", "30+"]
		        },
		        "type": {
		            "type": "select",
		            "removeDefaultNone": true,
		            "default":"ml",
		            "optionLabels": ["Rules", "ML"]
		        }
		    }
		}
	}
}