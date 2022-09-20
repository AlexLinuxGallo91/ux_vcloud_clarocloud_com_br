TIME_TOTAL_RENDER_PORTAL = 0
RESULT_PORTAL_RENDERED_IS_CORRECT = True
HTTP_TIME_TOTAL_RESPONSE = 0
HTTP_STATUS_CODE = 0


def print_result():
    print('Tiempo total del rendereo del portal: {}\n'
          'Renderizado correcto del portal: {}\n'
          'Codigo Http del response: {}\n'
          'Tiempo total de la peticion Http: {}\n'.format(
        TIME_TOTAL_RENDER_PORTAL,
        RESULT_PORTAL_RENDERED_IS_CORRECT,
        HTTP_STATUS_CODE,
        HTTP_TIME_TOTAL_RESPONSE
    ))
