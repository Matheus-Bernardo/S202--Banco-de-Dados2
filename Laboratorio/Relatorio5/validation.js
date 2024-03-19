{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'titulo',
      'autor',
      'ano',
      'preco'
    ],
    properties: {
      titulo: {
        bsonType: 'string',
        description: 'deve ser uma string e é obrigatória'
      },
      autor: {
        bsonType: 'string',
        description: 'deve ser uma string e é obrigatória'
      },
      ano: {
        bsonType: 'int',
        minimum: 1965,
        maximum: 2023,
        description: 'deve ser um inteiro entre [1965, 2023] e é obrigatório'
      },
      preco: {
        bsonType: 'double',
        description: 'pode ser qualquer valor float'
      }
    }
  }
}