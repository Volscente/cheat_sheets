# Datetime

## Current Datetime
``` python
current_datetime = datetime.today().strftime("%Y_%m_%d_%H_%M")
```

# List

## Chunk Lists of List
``` python
def chunks(lst, n):
for i in range(0, len(lst), n):
    yield lst[i:i + n]

# Read the data
self.valid_invoices = self.spark.table('uc2_d_analysis.km_interpolation_source_data')

# Retrieve list of fleetvehicle_id
fleetvehicle_id_list = self.valid_invoices.select('fleetvehicle_id').distinct().collect()[:9]

self.logger.info('run - FIX KM INTERPOLATION - Total number of fleetvehicles: {}'
                .format(len(fleetvehicle_id_list)))

# Define help variables
chunk_size = 600
chunked_fleetvehicle_id_list = list(chunks(fleetvehicle_id_list, chunk_size))
number_of_chunks = len(chunked_fleetvehicle_id_list)
current_chunk = 1

for chunk in chunked_fleetvehicle_id_list:

self.logger.info('run - FIX KM INTERPOLATION - Progress: {}/{}'.format(current_chunk, number_of_chunks))
self.logger.info('run - FIX KM INTERPOLATION - fleetvehicles: {}'.format(chunk))

try:

    interpolated_invoice = self.valid_invoices.filter(self.valid_invoices.fleetvehicle_id.isin(chunk))\
        .groupby('fleetvehicle_id')\
        .apply(km_interpolation)

    interpolated_invoice.show(1, vertical=True, truncate=False)

    current_chunk = current_chunk+1

except Exception as e:

    import sys

    self.logger.error('run - FIX KM INTERPOLATION - Error with fleetvehicle: {}'.format(chunk))
    self.logger.error(e)

    sys.exit(1)

self.logger.info('run - FIX KM INTERPOLATION - OK')
```

## List Comprehension with if-else
``` python
['A' if c[i] == 'B' else 'B' for i in range(N)]
```

## Count Occurrences
``` python
['A' if c[i] == 'B' else 'B' for i in range(N)]
```

# Objects
## Retrieve Object Attributes
``` python
# Instance the object
object = Class()

# Retrieve the list of Attributes
object.__dir__()
```

# JSON
## Pretty Print
``` python
import json
print(json.dumps(json.loads(json_format_variable), indent=4))
```
