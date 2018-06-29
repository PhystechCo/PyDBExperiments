BILLON = 1000000000.0

labels = {"NOINNO": "No innovadoras", "AMPLIA": "Innovacion amplia", "POTENC": "Potencial", "ESTRIC": "Estrictas",
          "INTENC": "Con intención"}

industries = {}
industries[ "Elaboración de productos alimenticios" ] = [ 1, 1000, 1100 ]
industries[ "Elaboración de bebidas" ] = [ 2, 1100, 1200 ]
industries[ "Elaboración de productos de tabaco" ] = [ 3, 1200, 1300 ]
industries[ "Fabricación de productos textiles" ] = [ 4, 1300, 1400 ]
industries[ "Confección de prendas de vestir" ] = [ 5, 1400, 1500 ]
industries[ "Curtido y recurtido de cueros; fabricación de cuero y similares" ] = [ 6, 1500, 1600 ]
industries[
    "Transformación de la madera y fabricación de productos de madera y de corcho, de cestería y espartería" ] = [ 7,
                                                                                                                   1600,
                                                                                                                   1700 ]
industries[ "Fabricación de papel, cartón y productos de papel y cartón" ] = [ 8, 1700, 1800 ]
industries[ "Actividades de impresión y de producción de copias a partir de grabaciones or" ] = [ 9, 1800, 1900 ]
industries[ "Coquización, fabricación de productos de la refinación del petróleo y activid" ] = [ 10, 1900, 2000 ]
industries[ "Fabricación de sustancias y productos químicos" ] = [ 11, 2000, 2100 ]
industries[ "Fabricación de productos farmacéuticos, sustancias químicas medicinales y pro" ] = [ 12, 2100, 2200 ]
industries[ "Fabricación de productos de caucho y de plástico" ] = [ 13, 2200, 2300 ]
industries[ "Fabricación de otros productos minerales no metálicos" ] = [ 14, 2300, 2400 ]
industries[ "Fabricación de productos metalúrgicos básicos" ] = [ 15, 2400, 2500 ]
industries[ "Fabricación de productos elaborados de metal, excepto maquinaria y equipo" ] = [ 16, 2500, 2600 ]
industries[ "Fabricación de productos informáticos, electrónicos y ópticos" ] = [ 17, 2600, 2700 ]
industries[ "Fabricación de aparatos y equipo eléctrico" ] = [ 18, 2700, 2800 ]
industries[ "Fabricación de maquinaria y equipo n.c.p." ] = [ 19, 2800, 2900 ]
industries[ "Fabricación de vehículos automotores, remolques y semirremolques" ] = [ 20, 2900, 3000 ]
industries[ "Fabricación de otros tipos de equipo de transporte" ] = [ 21, 3000, 3100 ]
industries[ "Fabricación de muebles, colchones y somieres" ] = [ 22, 3100, 3200 ]
industries[ "Otras industrias manufactureras" ] = [ 23, 3200, 3300 ]
industries[ "Instalación, mantenimiento y reparación especializado de maquinaria y equipo" ] = [ 24, 3300, 3400 ]

nivel_calificacion = {"10": 64,
                      "9": 66,
                      "8": 68,
                      "7": 70,
                      "6": 80,
                      "5": 74,
                      "4": 72,
                      "3": 76,
                      "2": 78,
                      "1": 82
                      }

nivel_inversion_ACTI = {"9": 53,
                        "8": 54,
                        "7": 58,
                        "6": 59,
                        "5": 55,
                        "4": 56,
                        "3": 60,
                        "2": 57,
                        "1": 61,
                        "0": 62
                        }

totales_inversion_ACTI = {53: "Actividades de I+D Internas",
                          54: "Outsourcing",
                          55: "Adquisicion de maquinaria y equipo",
                          56: "Tecnologias de informacion y telecomunicaciones",
                          57: "Mercadotecnia",
                          58: "Transferencia de tecnologia",
                          59: "Asistencia Tecnica y Consultoria",
                          60: "Ingenieria y diseno industrial",
                          61: "Formacion y capacitacion"
                          }

obstaculos = {39: "Escasez de recursos propios",
              40: "Falta de personal calificado",
              41: "Dificultad para el cumplimiento de regulaciones y reglamentos tecnicos",
              42: "Escasa informacion sobre mercados",
              43: "Escasa informacion sobre tecnologia disponible",
              44: "Escasa informacion sobre instrumentos publicos de apoyo",
              45: "Incertidumbre frente a la demanda de bienes o servicios innovadores",
              46: "Incertidumbre frente al exito en la ejecucion tecnica del proyecto",
              47: "Baja rentabilidad de la innovacion",
              48: "Dificultades para acceder a financiamiento externo a la empresa",
              49: "Escasas posibilidades de cooperacion con otras empresas o instituciones",
              50: "Facilidad de imitacion por terceros",
              51: "Insuficiente capacidad del sistema de propiedad intelectual para proteger la innovacion",
              52: "Baja oferta de servicios de inspeccion, pruebas, calibracion, certificacion y verificacion"
              }

importancia_innovaciones = {22: "Mejora en la calidad de los bienes o servicios",
                            23: "Ampliacion en la gama de bienes o servicios o bienes",
                            24: "Ha mantenido su participacion en el mercado geografico de su empresa",
                            25: "Ha ingresado a un mercado geografico nuevo",
                            26: "Aumento de la productividad",
                            27: "Reduccion de los costos laborales",
                            28: "Reduccion en el uso de materias primas o insumos",
                            29: "Reduccion en el consumo de energia u otros energeticos",
                            30: "Reduccion en el consumo de agua",
                            31: "Reduccion en costos asociados a comunicaciones",
                            32: "Reduccion en costos asociados a transporte",
                            33: "Reduccion en costos de mantenimiento y reparaciones",
                            34: "Mejora en el cumplimiento de regulaciones, normas y reglamentos tecnicos",
                            35: "Aprovechamiento de residuos en los procesos de la empresa",
                            36: "Disminucion en el pago de impuestos"
                            }
