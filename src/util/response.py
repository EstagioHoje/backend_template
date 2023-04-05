from django.http import JsonResponse, HttpResponseNotFound

class ResponseHandler:

    def GetSuccess(data):
        response = {
            "message": "Get Successfully",
            "data": data
        }
        return ResponseHandler._Response(response)
    
    def PostSuccess(data):
        response = {
            "menssage": "Added Successfully",
            "data": data
        }
        return ResponseHandler._Response(response)


    def PostFailure(error):
        response = {
            "menssage": "Failed to Add",
            "error": error
        }

        return ResponseHandler._Response(response)
    
    def PutSuccess(data):
        response = {
            "menssage": "Update Successfully",
            "data": data
        }
        return ResponseHandler._Response(response)

    def PutFailure(error):
        response = {
            "menssage": "Failed to Update",
            "error": error
        }

        return ResponseHandler._Response(response)
    
    def DeleteSuccess(data):
        response = {
            "menssage": "Delete Successfully",
            "data": data
        }
        return ResponseHandler._Response(response)


    def DeleteFailure(error):
        response = {
            "menssage": "Failed to Delete",
            "error": error
        }

        return ResponseHandler._Response(response)

    def _Response(response):
        return JsonResponse(response, safe=False)
    
    def _404Response(Data=""):
        return HttpResponseNotFound(Data)
