TIME_TOTAL_RENDER_PORTAL = 0
RESULT_PORTAL_RENDERED_IS_CORRECT = True
HTTP_TIME_TOTAL_RESPONSE = 0
HTTP_STATUS_CODE = 0
HOST_KEY_TIME_TOTAL_RENDER_PORTAL = 'time_total_render_portal'
HOST_KEY_RESULT_PORTAL_RENDERED_IS_CORRECT = 'result_portal_rendered_is_correct'
HOST_KEY_HTTP_TIME_TOTAL_RESPONSE = 'http_time_total_response'
HOST_KEY_HTTP_STATUS_CODE = 'http_status_code'


def print_result():
    print('Tiempo total del rendereo del portal: {}\n'
          'Renderizado correcto del portal: {}\n'
          'Codigo Http del response: {}\n'
          'Tiempo total de la peticion Http: {}\n'.
          format(TIME_TOTAL_RENDER_PORTAL,
                 RESULT_PORTAL_RENDERED_IS_CORRECT,
                 HTTP_STATUS_CODE,
                 HTTP_TIME_TOTAL_RESPONSE))
