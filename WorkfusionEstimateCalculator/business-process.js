var businessProcess = {

	"schema": {
		"type": "array",
        "items": {
            "type": "object",
            "properties": {
                "applicationType": {
                    "type": "number",
                    "title": "Business Process part",
                    "enum": [0.5, 1, 1.5, 1, 0.4]
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
                    "default":0.5,
                    "removeDefaultNone": true,
                    "type": "select",
                    "optionLabels": ["OCR", "Complex Splitting/Joining", "Lots of logic within data stores", "Business Rules", "Manual Task"]                
                },
                "complexity": {
                    "default":1,
                    "removeDefaultNone": true,
                    "type": "select",
                    "optionLabels": ["Standard", "Mid-Complex", "Complex"]
                }
            }
        }
	}
}