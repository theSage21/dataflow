$(document).ready(function() {
    Object.keys(programtable).forEach(function (key, index) {
        var button = "<li><button id='" + key + "' class='btn '>" + programtable[key][0] + "</button></li>";
        $("#operator_menu").append(button);
    });
    // ##############################################################################
     var boxcount=0;
     $("#addDD").click(function (){
          var operatorId = 'Data_Data'+ boxcount;
          var operatorData = {
            top: 0, left: 0,
            properties: {
              title: operatorId,
              inputs: {input_1: {label: 'inp1'}, input_2:{label: 'inp2'}, input_3:{label: 'inp3'}},
              outputs: {output_1: {label: 'out1'}, output_2:{label: 'out2'}, output_3:{label: 'out3'}},
              multiple: true,
              class: 'BoxDD'
            }
          };
          boxcount += 1;
          $flowchart.flowchart('createOperator', operatorId, operatorData);
     });
    // ##############################################################################
     $("#addSource").click(function (){
          var operatorId = 'Source'+ boxcount;
          var name = prompt("Please name this source:", defaultText=operatorId);
          var operatorData = {
            top: 0, left: 0,
            properties: {
              title: name,
              inputs: {},
              outputs: {output_1: {label: 'out1'}, output_2:{label: 'out2'}, output_3:{label: 'out3'}},
              class: 'BoxSource',
            }
          };
          boxcount += 1;
          $flowchart.flowchart('createOperator', operatorId, operatorData);
     });
    // ##############################################################################
     $("#addDE").click(function (){
          var operatorId = 'Data-Estimator' + boxcount;
          var operatorData = {
            top: 0, left: 0,
            properties: {
              title: operatorId,
              inputs: {input_1: {label: 'est1'}, input_2:{label: 'data1'}},
              outputs: {output_1: {label: 'est1_out'}, output_2:{label: 'data1_out'}},
              class: 'BoxDE',
            }
          };
          boxcount += 1;
          $flowchart.flowchart('createOperator', operatorId, operatorData);
     });
    // ##############################################################################
    if (typeof existingdata != "undefined"){
        var data = existingdata;
    }else{
        var data = {operators: {}, links: {}};
    }
    var $flowchart=$("#example_multiple");
    var $container =$flowchart.parent();
    // ##############################################################################
    $("#codepen").change(function (){
          var opid = $flowchart.flowchart('getSelectedOperatorId');
          var data = $flowchart.flowchart('getOperatorData', opid);
          data['program'] = $("#codepen").val();
          $flowchart.flowchart('setOperatorData', opid, data);
    });
    // ##############################################################################

    $flowchart.flowchart({
      data: data,
      linkWidth:5,
      multipleLinksOnOutput: true,
      grid:10,
      onOperatorSelect: function (operatorID){
          $("#codepenlabel").text(operatorID);
          var data = $flowchart.flowchart('getOperatorData', operatorID);
          if (data['program']) {
              $("#codepen").val(data['program']);
            } else {
              $("#codepen").val("");
            }
          return true;
      },

    });
    // ##############################################################################
    $(document).keypress(function(e) {
        if ($("#codepen").is(":focus")) {console.log("I do not know how to do NOT");}
        else{
            switch (e.which) {
                case 120: 
                case 127:
                     $flowchart.flowchart('deleteSelected'); break;
                case 115:
                     $("#addSource").click(); break;
                case 100:
                     $("#addDD").click(); break;
                case 101:
                     $("#addDE").click(); break;
                case 109:
                     $("#MAKESCRIPT").click(); break;
            };
        }
    });
    // ##############################################################################
     $("#MAKESCRIPT").click(function (){
         var data = $flowchart.flowchart('getData');
         data['scriptname'] = prompt("Enter the script name: ", defaultText="script");
         $.ajax({
             'type': 'POST',
             'url': '/savejson',
             'contentType': 'application/json',
             'data': JSON.stringify(data),
             'dataType': 'json',
             'success': console.log});
     });
    // ##############################################################################
    $("#addreadcsv").click(function () {
          var operatorId = 'ReadCsv'+ boxcount;
          var name = operatorId;
          var operatorData = {
            top: 0, left: 0,
            properties: {
              title: name,
              inputs: {},
              outputs: {output_1: {label: 'data'}},
              class: 'BoxSource',
            }
          };
          boxcount += 1;
          $flowchart.flowchart('createOperator', operatorId, operatorData);
          var data = $flowchart.flowchart('getOperatorData', operatorId);
          data['program'] = programtable['addreadcsv'][2];
          $flowchart.flowchart('setOperatorData', operatorId, data);
    });
    // ##############################################################################
    $("#addrfclassifier").click(function (){
          var operatorId = 'RandomForestClassifier'+ boxcount;
          var name = operatorId;
          var operatorData = {
            top: 0, left: 0,
            properties: {
              title: name,
              inputs: {},
              outputs: {output_1: {label: 'est'}},
              class: 'BoxSource',
            }
          };
          boxcount += 1;
          $flowchart.flowchart('createOperator', operatorId, operatorData);
          var data = $flowchart.flowchart('getOperatorData', operatorId);
          data['program'] = programtable['addrfclassifier'][2];
          $flowchart.flowchart('setOperatorData', operatorId, data);

    });
    // ##############################################################################
    $("#addscore").click(function () {
        var operatorId = 'Score'+ boxcount;
        var name = operatorId;
        var operatorData = {
          top: 0, left: 0,
          properties: {
            title: name,
            inputs: {input_1: {label: 'est'}, input_2: {label: "data"}},
            outputs: {output_1: {label: 'score'}},
          class: 'BoxDE',
          }
        };
        boxcount += 1;
        $flowchart.flowchart('createOperator', operatorId, operatorData);
        var data = $flowchart.flowchart('getOperatorData', operatorId);
        data['program'] = programtable['addscore'][2];
        $flowchart.flowchart('setOperatorData', operatorId, data);
    });
    // ##############################################################################
    $("#addtrainclassifier").click(function () {
        var operatorId = 'TrainClassifier'+ boxcount;
        var name = operatorId;
        var operatorData = {
          top: 0, left: 0,
          properties: {
            title: name,
            inputs: {input_1: {label: 'est'}, input_2: {label: "data"}},
            outputs: {output_1: {label: 'est'}},
          class: 'BoxDE',
          }
        };
        boxcount += 1;
        $flowchart.flowchart('createOperator', operatorId, operatorData);
        var data = $flowchart.flowchart('getOperatorData', operatorId);
        data['program'] = programtable['addtrainclassifier'][2];
        $flowchart.flowchart('setOperatorData', operatorId, data);
    });

    // ##############################################################################
    $("#addprint").click(function (){
        var operatorId = 'Print'+ boxcount;
        var name = operatorId;
        var operatorData = {
          top: 0, left: 0,
          properties: {
            title: name,
            inputs: {input_1: {label: 'inp'}},
            outputs: {},
          class: 'BoxSink',
          }
        };
        boxcount += 1;
        $flowchart.flowchart('createOperator', operatorId, operatorData);
        var data = $flowchart.flowchart('getOperatorData', operatorId);
        data['program'] = 'print(inp)';
        $flowchart.flowchart('setOperatorData', operatorId, data);
    });
    // ##############################################################################
    $("#addtraintestsplit").click(function () {
        var operatorId = 'TrTsSplit'+ boxcount;
        var name = operatorId;
        var operatorData = {
          top: 0, left: 0,
          properties: {
            title: name,
            inputs: {input_1: {label: 'data'}},
            outputs: {output_1: {label: 'train'}, output_2: {label: 'test'}},
          class: 'BoxDD',
          }
        };
        boxcount += 1;
        $flowchart.flowchart('createOperator', operatorId, operatorData);
        var data = $flowchart.flowchart('getOperatorData', operatorId);
        data['program'] = programtable['addtraintestsplit'][2];
        $flowchart.flowchart('setOperatorData', operatorId, data);
    });
    // ##############################################################################
});  // document ready
