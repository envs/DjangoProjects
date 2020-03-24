function Calculator (inputs) {
    this.inputs = inputs;
    this.estimate = function() {
        var businessProcessEstimate = this.doBusinessProcessCalc(this.inputs.businessProcess, this.inputs.projectType)
        var apisEstimate = this.doApisCalculations(this.inputs.apis)
        var rpaEstimate = this.doRpaCalc(this.inputs.rpaApplications)
        // var mlClassificationEstimate = this.doMlClassificationCalc(this.inputs.mlClassifications);
        var mlExtractionEstimate = this.doMlExtractionCalc(this.inputs.mlExtractions);

        var estimates = [businessProcessEstimate,apisEstimate,rpaEstimate,/*mlClassificationEstimate*/,mlExtractionEstimate]

        var effort = this.mergeEstimates(estimates);

       
        console.log(effort);
        this.renderEffort(effort);
    }

    this.mergeEstimates = function(estimates) {
        var merged = {};
        estimates.forEach(function(estimate) {
            Object.keys(estimate).forEach(function(key) {
                var v = estimate[key];
                if (merged[key]) {
                    merged[key] += v;
                } else {
                    merged[key] = v;

                }
            });
        })
        return merged;
    }

    this.renderEffort = function(effort) {
        var container = $("#effort");
        container.empty();

        var devLine = $("<div>");
        devLine.append("<span><b>Developer: <b></span>");
        devLine.append("<span>" + effort['dev'] + " Days</span>");
        container.append(devLine);

        var rpaLine = $("<div>");
        rpaLine.append("<span><b>RPA Developer: <b></span>");
        rpaLine.append("<span>" + effort['rpaDev'] + " Days</span>");
        container.append(rpaLine);

        var daLine = $("<div>");
        daLine.append("<span><b>Data analyst: <b></span>");
        daLine.append("<span>" + effort['dataAnalyst'] + " Days</span>");
        container.append(daLine);

        var mleLine = $("<div>");
        mleLine.append("<span><b>MLE: <b></span>");
        mleLine.append("<span>" + effort['mle'] + " Days</span>");
        container.append(mleLine);

        var smeLine = $("<div>");
        smeLine.append("<span><b>SME: <b></span>");
        smeLine.append("<span>" + effort['sme'] + " Hours</span>");
        container.append(smeLine);

        
    }

    this.doBusinessProcessCalc = function(businessProcessParts, projectType) {
        console.log("\n>>>>>>>>>>>>>>> Business Process Calculator")
        var estimate = {
            'dev': 0
        };
        businessProcessParts.forEach(function(businessProcessPart) {

            var totalManDays = businessProcessPart.applicationType * businessProcessPart.complexity;
            console.log("Total man days = " + totalManDays);
            estimate['dev'] += totalManDays;
        });
        estimate['dev'] = Math.ceil(estimate['dev'] * projectType);



        return estimate;
    }

    this.doApisCalculations = function(apis) {
        console.log("\n>>>>>>>>>>>>>>> API Calculator")
        var estimate = {
            'dev': 0
        };
        apis.forEach(function(api) {

            var totalManDays = api.applicationType * api.complexity;
            console.log("Total man days = " + totalManDays);
            estimate['dev'] += totalManDays;
        });
        estimate['dev'] = Math.ceil(estimate['dev']);


        return estimate;
    }

    this.doRpaCalc = function(rpaApplications) {
        console.log("\n>>>>>>>>>>>>>>> RPA Calculator")
        var estimate = {
            'rpaDev': 0
        };
        rpaApplications.forEach(function(rpaApp) {
            var numberOfTotalActions = rpaApp.numberOfScreens * rpaApp.numberOfActionsPerScreen;
            console.log("Number of total actions = " + numberOfTotalActions);
            var manDays = parseInt(numberOfTotalActions / 20) + 1;

            console.log("Number of man days = " + manDays);
            console.log("App type koef = " + rpaApp.applicationType);
            console.log("Comlexity = " + rpaApp.complexity);
            var totalManDays = parseInt(manDays * rpaApp.applicationType * rpaApp.complexity);
            console.log("Total man days = " + totalManDays);
            estimate['rpaDev'] += totalManDays;
        })
        return estimate;
    }

    this.doMlClassificationCalc = function(mlClassifications) {
        console.log("\n>>>>>>>>>>>>>>> ML Classifications")
        var estimate = {
            'dataAnalyst': 0,
            'sme': 0,
            'mle': 0
        };

        mlClassifications.forEach(function(mlClassification) {
        	var DOCUMENTS_PER_CLASS = 300;
        	var TIME_PER_DOC_MIN = 1;
        	var SME_HOURS_PER_DAY = 6;
        	var numberOfClasses = mlClassification.numberOfClasses;
        	if (numberOfClasses > 25) {            		
        		numberOfClasses = parseInt(numberOfClasses * 1.2);
        	}
        	console.log("Number of classes = " + mlClassification.numberOfClasses);
        	var trainingSetSize = mlClassification.numberOfClasses * DOCUMENTS_PER_CLASS;
        	console.log("Training set size = " + trainingSetSize);

        	var smeTimeForTrainingSetMin = trainingSetSize * TIME_PER_DOC_MIN;
        	console.log("SME time for training set (min) = " + smeTimeForTrainingSetMin);
        	var smeTimeForTrainingSetDays = parseInt(smeTimeForTrainingSetMin / 60 / 6);
        	console.log("SME time for training set (days) = " + smeTimeForTrainingSetDays);

        	// Time for training = 1 week
        	smeTimeForTrainingSetDays += 5;
        	console.log("SME time for training set including training (days) = " + smeTimeForTrainingSetDays);
        	var dataAnalystTime = smeTimeForTrainingSetDays;
        	console.log("Data analyst time (days) = " + dataAnalystTime);

        	// 
        	var mleTimeDays = 5;
        	console.log("MLE time (days) = " + mleTimeDays);


            estimate['sme'] += smeTimeForTrainingSetDays;
            estimate['dataAnalyst'] += dataAnalystTime;
            estimate['mle'] += mleTimeDays;
        })
        return estimate;
    }

    this.doMlExtractionCalc = function(mlExtractions) {
        console.log("\n>>>>>>>>>>>>>>> ML Extractions")
        var estimate = {
            'dataAnalyst': 0,
            'sme': 0,
            'mle': 0
        };



        mlExtractions.forEach(function(mlExtraction) {
            estimate['dataAnalyst'] += calculateDaEffort(mlExtraction);     
            estimate['sme'] += calculateSmeEffort(mlExtraction);
            estimate['mle'] += calculateMleEffort(mlExtraction);            

            function calculateTimePerDocSec(numberOfFields) {
                return parseInt(-0.01659203103 * Math.pow(numberOfFields, 3)  + 1.02530820805 * Math.pow(numberOfFields, 2) - 0.63765646188 * numberOfFields + 25.71135661941);

            }
            

            function calculateDaEffort(mlExtraction) {
                console.log("\n\t>>>>>>>>>>>>>>> DA Estimations");
                var nOfDocs = mlExtraction.numberOfDocs;
                var numberOfFields = mlExtraction.numberOfFields;
                var timePerDocSec = calculateTimePerDocSec(numberOfFields);
                console.log("\ttimePerDoc in sec = " + timePerDocSec);
                var timePerDoc = timePerDocSec / 60;
                console.log("\ttimePerDoc in min = " + timePerDoc);
                // SUM(education + qualification + QC)

                // 2 days. Depends on complexity and nunmber of fields
                var INSTRUCTION_EFFORT_DAYS = 1;
                var preparations = INSTRUCTION_EFFORT_DAYS + numberOfFields / 10 + 1;
                console.log("\tpreparations time days = " + preparations);
                preparations = preparations * 6;
                console.log("\tpreparations time hours = " + preparations);


                var qualification = timePerDoc * 0.8;
                console.log("\tqualification = " + qualification);
                
                var adjudication = (1.5 * timePerDoc) / 100 * nOfDocs + (1.5038 * timePerDoc + 1.98);
                console.log("\tadjudication hours= " + adjudication);

                var total = parseInt(preparations + qualification + adjudication);
                console.log("\tTotal DA effort hours = " + total);
                total = parseInt(total / 6);
                console.log("\tTotal DA effort days = " + total);
                return total;
            } 

            function calculateSmeEffort(mlExtraction) {
                console.log("\n\t>>>>>>>>>>>>>>> SME Estimations");
                var getFamiliarHours = 2;
               
                var nOfDocs = mlExtraction.numberOfDocs;
                var numberOfFields = mlExtraction.numberOfFields;
                var timePerDocSec = calculateTimePerDocSec(numberOfFields);
                console.log("\ttimePerDoc in sec = " + timePerDocSec);
                var timePerDoc = timePerDocSec / 60;
                console.log("\ttimePerDoc in min = " + timePerDoc);
                var qualificationHour = 2.6 * timePerDoc;
                console.log("\tqualification in hour = " + qualificationHour);

                var taggingTimeHour = nOfDocs * timePerDoc / 60;
                console.log("\tTaggingTimeHour in hour = " + taggingTimeHour);

                var totalHours = parseInt(getFamiliarHours + qualificationHour + taggingTimeHour);
                return totalHours;

            }


            function calculateMleEffort(mlExtraction) {
                console.log("\n\t>>>>>>>>>>>>>>> MLE Estimations")
                var successCriteria = mlExtraction.successCriteria;

                // MLE effort.
                var SIMPLE_FIELD_STP = (4.1667 * Math.pow(successCriteria, 3) - 25.0000 * Math.pow(successCriteria, 2) + 5.8333 * successCriteria  + 115.0000) / 100;
                var MID_COMPLEX_FIELD_STP = (3.3333 * Math.pow(successCriteria, 3) - 20.0000 * Math.pow(successCriteria, 2) + 16.6667 * successCriteria + 40.0000) / 100;
                var COMPLEX_FIELD_STP = 0;
                console.log("\tSIMPLE_FIELD_STP = " + SIMPLE_FIELD_STP);
                console.log("\tMID_COMPLEX_FIELD_STP = " + MID_COMPLEX_FIELD_STP);
                console.log("\tCOMPLEX_FIELD_STP = " + COMPLEX_FIELD_STP);

                var MLE_EFFORT_SIMPLE_FIELD_DAYS = 0.5;
                var MLE_EFFORT_MID_COMPLEX_FIELD_DAYS = 1.5;
                var MLE_EFFORT_COMPLEX_FIELD_DAYS = 3;


                var numberOfFields = mlExtraction.numberOfFields;
                console.log("\tNumber of fields = " + numberOfFields);
                var fieldsComplexity = mlExtraction.fieldsComplexity;
                console.log("\tFields complexity = " + fieldsComplexity);
                var parts = fieldsComplexity.split("/");

                var simpleFields = parseInt(numberOfFields * parseInt(parts[0])/100.00);
                var midComplexFields = parseInt(numberOfFields  * parseInt(parts[1])/100.00);
                var complexFields = parseInt(numberOfFields  * parseInt(parts[2])/100.00);
                console.log("\tSimple Fields = " + simpleFields);
                console.log("\tMid-complex Fields = " + midComplexFields);
                console.log("\tComplex Fields = " + complexFields);

                var mleEffortDays = 0;
                mleEffortDays += simpleFields * (1-SIMPLE_FIELD_STP) * MLE_EFFORT_SIMPLE_FIELD_DAYS;
                console.log("\tSimple fields MLE effort days = " + complexFields);            
                mleEffortDays += midComplexFields * (1-MID_COMPLEX_FIELD_STP) * MLE_EFFORT_MID_COMPLEX_FIELD_DAYS;
                console.log("\tPlus mid complex fields MLE effort days = " + mleEffortDays);            
                mleEffortDays += complexFields * (1-COMPLEX_FIELD_STP) * MLE_EFFORT_COMPLEX_FIELD_DAYS;
                console.log("\tPlus complex fields MLE effort days = " + mleEffortDays);            
                mleEffortDays = Math.ceil(mleEffortDays);
                console.log("\tPure MLE effort days = " + mleEffortDays);      

                mleEffortDays *= mlExtraction.numberOfPages;
                console.log("\tMLE effort days with numberOfPages factor = " + mleEffortDays);      

                mleEffortDays *= mlExtraction.documentFormat;
                console.log("\tMLE effort days with documentFormat factor = " + mleEffortDays);      

                mleEffortDays *= mlExtraction.language;
                console.log("\tMLE effort days with language factor = " + mleEffortDays);  

                // 500-> 1, 1000->0.9 3000->0.8
                var nOfDocs = mlExtraction.numberOfDocs;
                var numberOfDocsFactor = 0.00000003 * nOfDocs*nOfDocs + -0.000145 * nOfDocs + 1.065;
                console.log("\tnumberOfDocsFactor = " + numberOfDocsFactor);      
                mleEffortDays *= numberOfDocsFactor;
                console.log("\tMLE effort days with numberOfDocsFactor = " + mleEffortDays);     

                mleEffortDays = parseInt(mleEffortDays);
                mleEffortDays += 2;
                console.log("\tMLE effort days with troubleshooting and setting up use-case = " + mleEffortDays);     
            
                return mleEffortDays;
            }
            
            
            
        });
        return estimate;



    }








}