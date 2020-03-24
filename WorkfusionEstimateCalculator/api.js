var apis = {

	"schema": {
		"type": "array",
        "items": {
            "type": "object",
            "properties": {
                "applicationType": {
                    "type": "number",
                    "title": "API Type",
                    "enum": [1, 1, 3, 2, 1, 2, 3]
                },                                                  
                "complexity": {
                    "type": "number",
                    "title": "Complexity",
                    "enum": [1, 1.5, 2.5]
                },    
            }
        }
	},


	"options": {
		"type": "table",
        "label": "APIs",
        "items": {
            "fields": {                
                "applicationType": {
                    "default":1,
                    "removeDefaultNone": true,
                    "type": "select",
                    "optionLabels": ["Excel", "Mail (SMTP)", "Mail (Exchange)", "Shared Folder", "REST", "SOAP", "Read files from Folder (Windows)"]                
                },
                "complexity": {
                    "default":1,
                    "removeDefaultNone": true,
                    "type": "select",
                    "optionLabels": ["Easy", "Mid-Complex", "Complex"]
                }
            }
        }
	}
}