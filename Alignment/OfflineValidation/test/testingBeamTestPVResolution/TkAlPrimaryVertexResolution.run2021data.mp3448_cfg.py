
import FWCore.ParameterSet.Config as cms

process = cms.Process("PrimaryVertexResolution")

import FWCore.PythonUtilities.LumiList as LumiList

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",
                            secondaryFileNames =secFiles,
                            fileNames = readFiles
)
readFiles.extend( [
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/0e0359a4-f3ec-4cce-a8fd-293413b3ae62.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/30e2919e-3e6c-482d-8f53-147776a2ec04.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/45b16915-76e8-49c1-a74c-099aebdab7b8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/9f538edb-640d-40cd-a594-3223db4bfaa7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/ac004bd1-3298-4497-9ba8-1cc845d3e772.root'
] )
readFiles.extend( [
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/389/00000/f426d556-9380-4eb3-8ebd-1e46df791d08.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/394/00000/d4665a6b-4e23-4de3-9172-66bb2312c52d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/1f9e2f81-3a3a-4007-a6f4-10e7b8f4f2a2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/4921e162-96ec-46ab-a1b9-e787e65f64f3.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/62dba840-f4b1-4d60-9760-de1eb365229a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/a9c32853-b769-4809-bdd5-b887f103c1c5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/c1d9cc6c-c702-4b09-bc60-4c05fc2ef9f0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/ce21b4a6-1de4-4e8f-b1a4-df36b266c316.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/395/00000/d388101e-37ce-4dbe-8dea-999169eb720e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/19a17a4c-f4c2-4f53-856d-b631df804777.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/1af0a581-50ca-415b-95e2-09a242993938.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/380c6182-3f14-4748-b6fe-12c295df9fad.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/389c77f8-17a7-4a1c-8ea5-3c320f9e4711.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/7a147400-500d-4eed-bd1f-a274bb1cebe8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/7f3c8fec-59b1-43a8-82a2-84cdce8adb8f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/86f21a9b-4b77-4629-8081-abdedcd5cb1c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/8d88eab6-7b52-4bbc-b450-d263800936d1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/955adb46-3a62-4486-be74-1fa609f111d6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/a2b00e8d-4cf3-4a08-b317-cc6f6f11744e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/a441e34d-a506-4e67-8a79-a34d5fac3af7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/a849abb6-37d1-4f1c-979a-1a55193fe918.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ac192233-f347-43b7-8263-34f74da03751.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/bf06fc08-6afc-4899-af43-5006a9a497c5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/bfa02fe2-bd9c-45b6-9a48-5267377a8909.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/c058fb7b-c23f-47e6-83f8-8080b5de54c8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ce599639-ce06-485f-ac70-d32992fbe613.root',
#'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ceff9b5c-0dfc-44a4-9d5e-3912034c46fc.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/dd074505-45f3-42f9-8f50-14c012767a45.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/396/00000/ea43c9a3-f1e1-441d-ae27-22286535e6b1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/5a5897bb-66f5-4756-8d7f-85fba5689f80.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/6a9ed916-b190-401d-ab64-b2cdbeb5cedd.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/a8272baa-3e60-473b-b5ff-a91d7c429f05.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/b724f4d1-b906-46c8-a7cd-a09d04b28e5f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/bfc435ab-0579-4995-98c6-808b79593da2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/d4e9a1d7-6b64-4bac-b201-cc518d21fde7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/dcef1def-a8ce-44ed-8d3b-8bf95d50c875.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/398/00000/f43f8bd4-c7d3-4b4b-a1ce-54ad9e649544.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/445/00000/2a588e22-8330-40b0-b4ee-c7efe166a8f2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/3abaabed-a8a2-48c8-a1a4-14f1599a9e1d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/5a13d3ab-2d99-4f69-bc5d-68e74a8c720c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/65f7e84d-1744-4fc6-ac8f-e68a47db51d2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/6f686254-4760-4aca-84b5-23ba74f24e9b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/b9129a15-0310-4896-bb6d-c348c199ef4c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/c5a72679-69f6-41d6-ab1b-5f97bc1305ac.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/cbb20205-2083-4ac3-94ab-4bfecb427c7c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/446/00000/eabdca47-8058-48d9-a41b-c4b42d276382.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/09a9446e-b0b2-4bdb-9f9d-49c87424daf5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/1bf181f7-e2cd-4193-927b-0637478d1307.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/1d4c65cc-7127-456f-a271-5fcc9698952b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/2e74860e-cce1-4723-a428-f541b5c6eca2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/2ec0d92a-76c9-4ad0-85ac-3a0e018a8fe6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/3ad5d3d4-10b3-42dd-9391-08e2034da218.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/5634f95b-54b7-4308-bf25-f2c28f2a7719.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/660a79cb-664a-4117-b399-aa34c3c6a4e3.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/6b84471e-2be2-4ac6-8e24-08d3dc7dff1a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/74d604f8-6733-42d0-8187-c8cedc406c1a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/8c0cd6c8-ce95-426c-aa9d-a95f31d0d38e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/b6293037-709c-479a-b64b-c0be5417d567.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/c3e1fb2c-ede8-4899-beb1-2aec49547160.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/cec3e5da-6d2c-4ec4-86a7-7173d074cac8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/d5da0c1d-43c4-42d8-b626-238357824d53.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/daf2fd59-1855-4a13-84cb-95b5e0b1998e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/de33c95c-3028-4614-8df9-7a964bde669e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/ef520769-3f19-469a-a0dc-2e838cea0f0c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/fce50d86-29a9-4cd3-bbee-a7c68509ff39.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/447/00000/fd9f7286-e3ff-4e7f-be9b-60f3d4ca5c95.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/36d13358-8731-459a-9c98-40db7bfdd5c5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/3af06783-7603-42f6-8bb4-3b1ec3621dea.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/9e2aed23-6701-47ba-b722-b6eea1ba12e5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/c8c12e35-0164-4a35-bcf7-40784bd797b3.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/df12fa1a-27b7-4075-8dee-6684ab6d667c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/e02e6be4-e4fc-4266-90b2-30de98b3324f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/e05e970d-a31c-4471-b89c-6104e14667b6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/448/00000/e5845561-f4ba-41a3-97c9-c69a90446ab0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/449/00000/245f28c7-f4de-43ba-ab77-ba78c8f9a140.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/449/00000/4977fcd0-fbe3-4c4d-97ae-d2329cfb3a9a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/449/00000/fe894806-2807-4400-bf82-f24258a8c732.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/0007b076-d4f2-475f-841f-3b1ecf01ffa5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/1250f6eb-0add-4daf-a430-6540a50c6c0b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/1615866d-5b94-4a46-890a-38762c4d5a4b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/36217bd6-11e3-43b1-b7b3-82f192baf9a9.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/36bf0700-17c5-4d15-86c6-845038c87942.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/3b3e9f5d-3322-4d87-bb51-5b3ccdfd67f8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/3b4a8698-dfc8-4f7a-852f-562571e75799.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/3fbacd19-8321-46cb-8ed0-a4d106bcfefb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/499675d4-c63b-4408-ac4d-a42aa19dbd01.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/5ee69a11-2947-4cc1-945f-1066349059e5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/60405113-ff37-4f34-adbc-cb8537bd62b6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/60d4eadb-df33-48fe-8845-34c1affffddc.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/6adfaa5f-befd-4dc1-adf1-bc793438887d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/6c4f74f6-5f1b-4af5-8fa4-658583e97685.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/6dec3d15-47e9-485d-a402-b6f1f8655992.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/712dea1b-7e00-43ca-8760-55c9cf584253.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/72cf5ba1-ca10-422a-8376-d5b01a990317.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/78e1f8c4-adc2-4d47-bd51-19fe8daf0548.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/7a53907a-9dd1-4a4b-9441-f81441c91d02.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/7d9cf29b-05b2-45ed-a34a-b11177743df0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/83b07961-dbcf-495e-bb3b-ed92b8934aa8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/863322f4-35fa-4f10-8992-c025e5a7c5e0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/884945ad-c60e-43f2-818b-1bf40b1672e0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/909d1160-2908-4bd6-94e1-3d821aa9e53b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/a7f5c2f5-5234-49df-bcd0-0e7b54145178.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/add72d78-be96-4150-8834-8b6d928432e1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/b09eb1f1-b3e1-4210-90f3-402c0c6ff20c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/b50c1b1d-ce94-4175-83e9-7c8d355acfd4.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/c3650b55-e5c6-411c-a46d-b55cdd8e6691.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/c7e0eb33-74ff-4719-bee1-e21c68f1825f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/d227e591-2bbc-4cf3-b2e3-14a3090e59fb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/450/00000/fb94e81d-b08b-4410-bf68-42f02cb61d59.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/008ae1ce-b0ae-4ef7-bef8-50f3e8780fdd.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/0093fbf8-2e77-4a1b-b797-d8a611267d39.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/17e55daa-0cbd-4dbd-ba1a-2431a7ecee09.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/1fc4ebdf-41fb-4552-8189-9a299c31520c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/236688c7-a603-499d-8008-70c619f05268.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/2c69465e-d9d6-455a-9feb-1cceb350d477.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/2ee1b020-e578-4a0a-a743-2c6bc1febf7e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/2ee20819-d244-41e7-9b0c-7545d65514ba.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/330546ca-e9f0-4d56-889f-03669a7e7597.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/3b032d76-4e19-4f29-a07e-97422bf0c8b6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/4b0bb8e0-0192-4113-9053-4025eba8452a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/4f1b8250-1e95-4c91-8c8f-f214618b26ce.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/5c7521d4-4506-4df0-b186-227ac5d44d90.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/6dda8619-e3d8-425e-8749-8217a56a20d9.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/6f7fa6eb-9f68-4ccd-b26f-f2f9941fe0f6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/706aed0b-6775-46fe-acd7-5d2034ba687b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/7878dba2-9988-4760-a9a2-3c8d7d1126cb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/794d7f3f-d2f6-4329-a3c7-d82d72190392.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/7b8bdcf3-18ec-4453-8175-32afbf9c9ec9.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/80c96dc5-5381-4bd2-a235-f3232dd40a0c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/85ae55b2-587b-4f70-98c2-871cd0f96415.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/93bc2fdc-b706-453e-8e8b-bdfa7b5a21e4.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/9c59378a-4981-4408-81c4-eaed9266ee09.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/a227f56e-2c4b-4075-9f3c-8b8ff5022a4b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/afe15395-de31-4506-bc15-b5b45269f9b3.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/b835b6e7-7544-42f8-9ce4-8691fa6e3fb5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/bc35d8c3-89e6-44a9-9f61-25d7effe4d08.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/bc523fc8-da59-47eb-a446-d18b58446eac.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/d1c9262f-0c05-4b7a-9364-75ba54d5961c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/d84711d1-7d20-48ad-ad62-47dbb37ccb91.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/df3699bd-bd5e-48e3-9687-48fdcd3eb523.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/452/00000/e02ce573-5368-4a1c-8c6e-2564e1309229.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/0082d997-bb35-4677-9a9f-da6240e240c2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/29455d6e-4509-420f-886f-d95f58a45798.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/66d17d74-fb46-4df6-a532-09475a2b2c7b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/6f8abc48-87e4-4c08-9930-14139098cd78.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/90d403e7-132e-4635-bbff-be9dfcc077d6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/a2cbae38-7943-4b4a-a4e5-f510b3483e33.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/a3189ce5-16fe-44b4-8228-83815e5326a1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/d2db9194-e045-48af-acdd-82cfe29c6367.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/453/00000/e71c9306-a08b-420c-bd4d-bcf30589fb5c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/008589df-467a-4f7b-a0c7-584ea220751d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/04302012-d4d4-4e42-8006-4bac3aa5e637.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/0454d44f-7ab9-4bad-9989-b30f2fa7515c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/1365693f-ba7e-4a6e-a7f0-85a98393ccde.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/295ae701-5cce-4933-af36-71d4efdd9cb5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/2c8d88f3-a127-4139-982e-5af9944ddd26.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/387eb5e8-85e7-4fe5-b996-35259c45944f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/3c3ef18b-ee6d-4330-b135-33281f3bd404.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/3decefd6-c944-4c44-8dbb-badf657748fa.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/4b3c175c-db5b-4dad-9aa1-1b7d5dc07eea.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/6420f47a-f0fa-4ef7-a4fe-6eb77c85ef63.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/6856d04b-e6c3-4141-8021-d212a0eedded.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/86ac8d2b-1c28-423f-a0fc-64a32192fca9.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/86ad5eb1-2686-483c-9776-bb9dec9e0360.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/98ca3d73-6bbf-4099-a0fd-2ad556dc02c0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/a130ac59-1f31-4f8b-aa22-bcdb5d3d51bb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/a6f21be9-9bbf-4bd1-acc1-9a6bfdcb9bb9.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/a8dd7102-2c6e-4dac-8d10-35f0036f3323.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/ab213cf3-ba45-44cd-972b-c5920d7b3237.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/b103a6b5-c1c4-4b53-b5ff-8039e32ee6b3.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/b3312894-db2d-4779-91da-25701d1eccb8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/d8f0d074-eb19-4cf4-a017-98c86452dfa8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/d9dae0b9-30bd-4e24-900c-5de508640833.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/e9f9fcfd-458d-4393-8f69-f7fd6f0b8745.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/455/00000/f27ce0d3-9281-4acb-91c3-a8e5855e3568.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/519af03f-ce9f-4011-9c90-07177e9730ba.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/60bfd632-7ae9-4eb1-b672-6f3db39b802e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/8e211e05-73c5-40c6-bc04-b525e919bd38.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/a008e4ea-894e-4203-a551-089f39e91e83.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/ca7b847e-0cf3-4ff9-9cbd-1a0dde696d7a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/cb40c84b-5bf4-4687-b5c1-ef4c630560ea.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/d99efbaf-78a7-4dcf-bbf7-ec7205908020.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/483/00000/e4e06986-7604-4d06-9152-7319fe17e9dd.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/0d867165-03b9-40cd-9e70-9c25fde23e66.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/433aa3a5-e081-4524-84fa-433959501ea6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/60b8daee-e950-45a0-a598-9963d8cf1e8f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/6e2e553f-e7fe-43b2-8a8b-fedec091aad4.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/79a38056-c810-4883-96e1-5bc1892426b8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/a183a35a-6719-429c-94fd-50395077870a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/a7824351-e6e9-4d7f-9fe0-82352282a363.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/484/00000/ccad121e-a608-4665-bd00-306279b043b1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/485/00000/4c2a403e-9323-43a8-9b1e-11386609d3cc.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/485/00000/a7a838cc-6a76-4072-91c5-0b1105945ca0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/485/00000/b60e2e8b-ff61-4318-9057-b2e67980f81a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/485/00000/de8e41d1-0f56-42ce-8b71-dd7157e413ec.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/112a6b6d-8d3c-4961-81c5-1371598ed87c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/1ca5f69e-4adc-4f13-9159-5b1b571c440c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/6204755a-2351-4029-afb0-71ecebb1af2b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/70f290fe-842e-4a71-aaaa-05f747e7cefb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/729337f3-0f7e-43ff-b7e5-e02c88c0e6d8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/b05ba563-4268-4dc6-b913-37c0a1a112d7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/b286cf8e-b3fa-4be5-815a-1645ffd387f7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/c6d4758d-1533-41c9-a71c-dee9bfd98963.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/486/00000/dba28cc9-7030-4d41-9bfa-84417bede44d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/243b622c-2295-4e65-8579-93104cbff299.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/2ab59f69-79cc-498e-9b60-4d1771451668.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/2c254d05-c5b5-442a-96f8-2e4e3b78ec9b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/57646e4d-d224-4a57-a91e-2572272a1a07.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/60580696-25b2-4243-bc0e-64c706682f78.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/ae6433c9-21a2-48d3-9ad4-6a81c345b69e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/cd8afc30-ffa5-49c4-83a1-e443d79430f8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/f3392217-30b7-4942-b315-7ed1f3495368.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/487/00000/ff0057e1-7404-4b9b-a552-4747fc8826d1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/488/00000/34830f28-7e0c-46c6-8549-b2049857795a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/488/00000/3cd9013d-b334-475c-9654-fa1425f3a300.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/488/00000/460950bd-de50-4ae9-93b9-6cb3cab45243.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/488/00000/67315318-2d53-4ce1-b8b3-766e3104c629.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/488/00000/9c88bc3e-6f74-4dc3-ae97-72a7082393b2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/488/00000/cacacee7-cd7f-4f05-b581-d753ca058b65.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/488/00000/f7f39cdf-96e3-41d8-9910-cf26ba9a4110.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/019291f2-7477-4a50-bf2f-c97b3c4de0ee.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/04e9d3f9-d82f-4506-b053-00c96b643023.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/089f5318-60ed-4fab-8855-ef9c970f3b01.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/155b39c8-d900-4215-b51c-083825224807.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/180b2796-7217-4b9e-a581-35be562227f0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/192f6333-4659-45b1-b6a4-177ac0cf3985.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/213bb2da-9998-4805-b624-17a9dcd7d5a1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/26befc5c-cbc8-4cfa-9306-8416824454be.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/283b1414-69a7-4e9b-89d7-c6fdf4d4aa91.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/2e96a6ff-2b5f-4a40-92a3-676afd7fbf59.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/325f4b6c-dee6-4c56-b30e-9740fc151149.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/359770b7-e395-4400-9a16-68c99503775e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/37f9b58f-0ea2-4deb-a7be-d438a5fe7ee4.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/3b19d6ce-e682-4ffb-825c-66a4c6555970.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/3e73c295-18fb-4e12-9966-0c001ff31652.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/3f204473-636d-41fb-b138-3e7ed6352df8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/42f23bcd-db3c-4e79-a64f-ba97a21db28d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/470bc9c4-3fa6-4251-aa83-1f47b4dd7712.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/47833e41-4899-4538-a5dc-4272804eea1c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/47f06af4-7ba9-4d64-b848-f0198f1cfb3a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/49519ac5-ff1b-420e-8fc7-16eedb3c59eb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/4ecb15c0-dd7a-4a4a-a92d-fd34953939eb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/5102a6e4-924c-4f49-9d7e-06164f53cfdb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/51f1cb6c-5422-4b2f-a521-b47274fcd49b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/5efc2ae3-7253-445b-b57b-adc6f20357e0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/6440a158-d63f-46cd-a0b4-62ffee264083.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/64506fa9-0744-4010-a51b-ac3a92d23b4d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/6727385c-f299-4733-91d4-031cb5770c97.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/7f3bccf7-b3fe-465f-b23f-e06989078a24.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/809c5403-a581-47fb-9960-dc5da9faaafa.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/849918cf-55b4-4f0e-809f-3d0e4ab26b88.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/84ac7143-1082-40c6-a731-27e9f3ccee41.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/877cd734-3337-4bb4-a79a-698c879156b3.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/9337a2c5-50fc-4a8b-bacb-054dc0f3629e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/97c5dea2-df6e-44dc-b24e-a0e80d3d0c03.root'
] )
readFiles.extend( [
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/9b1369de-6c6f-428e-a0c6-ce6b79b20bc5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/9f573786-b630-41b9-9a51-fc8438c4843b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/b4e28ac7-bd12-4321-8fbd-136e958801aa.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/b87d9ba9-7fbe-434d-953a-9dc443da5ab2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/ba37afd5-2ebd-408a-97b1-3eadec4608c8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/d5ca3d2c-cf7e-44f3-b2fb-26252a28ca50.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/d76ffd4d-9217-42ca-813d-f8155ed6d797.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/e16754ca-18b4-4d79-932c-272b80ef3956.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/e5ddbb27-30a6-45a2-a388-bedae87a0713.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/e88524f1-3379-4f1d-bcf6-4568ba2877ed.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/ecd22620-4a11-484f-b03a-0f9eec331233.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/ed76e8a2-c113-4564-b2ab-481502121005.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/fa788c43-ee79-4a7b-9431-24d291bd6158.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/fdb4535d-7c4c-47bb-abea-6d30d79ac2b1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/fe09d129-bc4f-4e35-8506-3333a51cf111.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/490/00000/fead5588-6eab-4582-aa24-20d772b9c1f2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/0e651d5b-1a45-47ce-bc61-bcb8a3849039.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/104071a1-96f3-47a6-a047-353db3cbd0ed.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/142982e5-371d-4b28-8653-a89a03badd99.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/1c23c14a-1a9a-4f6a-9097-c90b1a8aa4fd.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/219e52e1-bb8c-469a-b2ab-adf019038d8e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/2265d603-8f62-45bc-83e7-55636cfbae7b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/29083e64-1132-43ef-b911-4600fc2166c6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/3336776d-071c-4c85-bb58-ac6949bc1ffa.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/35ddd11e-5e2c-4841-89fb-d919384b1ff8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/3a659ecf-4d19-479a-91f2-afcf09164cb9.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/3f6b3411-e317-4893-8d84-0b5acea2c7b2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/4adc8642-b610-40a9-ba9d-1bf31569f6aa.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/4b9715ad-ba81-4a3c-9f83-ff266272fd09.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/4c6b2101-10ba-4582-b414-da8934322304.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/4d1798b3-9f5a-4058-9f66-e4ca756faedb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/5410184e-b9ab-40ef-8ceb-62a75259b01b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/56c13f4d-0e72-490f-9757-54952ae6740e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/5954f6b5-2096-41f8-9a39-1f18db2dc9b3.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/5bc8314c-011d-4027-822d-ec4de345eb7a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/64aba5dc-4323-4678-ad81-908a293bb072.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/650b7cc6-6160-42c5-8426-70774c8e4866.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/66b405f9-25e0-432a-bcff-786aff23d730.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/675901a8-cf75-4564-8b8e-f091c9c82f2f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/71b308f4-ba0c-4af9-acad-f38a6fe781c0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/78d7fa59-0d31-4f63-a1dc-94bc2edb2b92.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/7ac84332-35ef-4618-af93-8e32d34d24fb.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/8b6b6848-e362-4111-bb56-46b27a1b5a34.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/92bf79d6-a6e2-4859-ac72-d49f7dff1bd5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/9412fee6-1e03-4988-a62b-f92237b69f15.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/9db6db92-0cb8-4d19-b4f2-819adc0bd00f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/9f856f4d-514e-4390-b1e4-ef0f8b82c1c2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/a02b1156-79e8-4ce2-abbb-bcdfcd1975a0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/a0c23221-c6d5-4633-9ca8-3fbbecd3b3c8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/a1258ac5-ee99-427d-8d98-d1dce3b939d7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/b1c645a6-2d9a-44a0-b1d4-066efc55ee77.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/c8499e78-b7d3-46d7-83d7-e733fdb01f1a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/c86ba2bb-4df7-4c85-bce5-ead7dde781e6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/ca499e52-df94-41c9-8a7f-c5ecb0cefa25.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/dceb42c9-55c0-494e-9a6d-ee6f353bcf2a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/e90403c7-908b-4f58-b27b-13e9c035f669.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/ec694066-da60-4bad-8a6d-f46471748d70.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/f1611a78-cc06-4a00-8d9b-ff43925df664.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/494/00000/fe821dd9-57f9-4251-a8e7-23779e9e49b7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/506/00000/18d1c6a3-4a05-40ba-8431-d7a0e7cdcab4.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/506/00000/9a01a800-5d40-483a-983a-e9dbb63ea365.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/507/00000/0e09f19d-d619-42a6-a0da-1bf6e2a6ba25.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/507/00000/1b4b295f-23cb-4d0f-a67b-64907ecc1790.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/507/00000/2b9a1d03-7cc7-4103-bfaa-9778ccdd03b4.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/507/00000/4b43a086-0b44-4a66-ba68-0bc0ea3c93bd.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/507/00000/e8246341-2931-462f-8e12-f63c6dbdf082.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/508/00000/46a3de04-6226-4abc-99ca-847cf3699286.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/508/00000/8a3d1e98-f0c6-404b-9b91-30244fc30921.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/508/00000/b436b28c-811a-4a94-aa4c-9c84f0cc9ec6.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/508/00000/c882772a-48d1-4360-b27c-9d102528510b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/509/00000/3c2e725c-5361-4db3-b66a-7a9eb7f180d8.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/509/00000/58c2450f-f459-49c0-9452-329512543350.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/509/00000/81de0a92-cb21-4548-8e3f-f6161456945c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/509/00000/b09c7450-3253-4be1-aade-6e05f0e1d956.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/509/00000/fc29fb69-18dc-4022-b77c-3cb93ef2a7ef.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/510/00000/409a284f-cece-416d-8cd7-35af7d83b78f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/510/00000/558bbfe8-408f-4020-bc53-2ae0804c705c.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/510/00000/84cb0d3d-9b70-4198-bf6e-64507344823e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/511/00000/1281a4ba-3e2f-4543-9255-04026299acc1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/511/00000/7df47829-b0e3-4320-91a0-c9357c0a2398.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/511/00000/c934d5c4-05c3-4911-b5ec-51e1366bd58f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/511/00000/ebf6779e-6390-42a1-b6cf-63394009ece1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/0e41c0b3-ef9c-4c04-8f04-98a35e98a9ad.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/0f43eeb3-aa6e-440c-8e6f-f4677e4ae039.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/15159440-a02a-471a-a341-84f17b2a8e93.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/15c8878b-b0bf-46c1-9dce-924e6d3c0d30.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/17f0e907-7b7a-48e2-9a5a-fc4816b07b6d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/194fdde6-b2fc-426a-9c1f-0c2b84b67a64.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/287b3324-36d1-4191-8fe0-061960b7ec5b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/2a2c978c-1a22-44e0-84fe-c26b7ac4f777.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/2b51e17f-fa8d-421e-af60-22c677c21d0f.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/2da1ae0a-828d-4dad-a0c7-c57f247fb619.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/3994c600-3194-4f94-91b6-6692ff6d8a33.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/3c5236cf-4f08-4289-b0af-8de949306197.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/3edab6c1-a5f5-4ab4-8ee2-518c18793d88.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/3fdaf178-05b5-4cf9-8ba0-50a93fe5e6c4.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/40981a34-8f16-404d-a7a6-aed79c551cd7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/420da306-e1d3-4a29-b608-61ef234d1595.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/57bd10ea-8f21-4229-b37d-28eb1349d3da.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/5e633dd3-1bc5-4372-a877-bb54f4fa282d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/672f8e71-cf03-4907-81a8-25edd14f7237.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/6ea6d828-3083-47a4-8f58-ec82fd3cdba7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/6ef3e92d-1aba-4171-9c18-fe57d001aee1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/70c83e71-4a03-4ad7-a308-cb2c4ca1a271.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/74c6eadf-9a3b-4a02-8e79-da096fff64e5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/762f2a29-0f5e-4d7e-9b6b-48b7c4f5669e.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/80b3ebee-72d5-4a01-a421-1276c075096d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/814d4799-7a6d-4dd4-aa95-5f289aa8a787.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/839b9a78-749d-4cc9-b977-2ea06ed37a5b.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/855bfb0c-730a-45e6-91eb-1595e898ab60.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/8e1952af-713e-48b4-bcba-67aa2d1b4bd1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/93803d6b-f074-449e-8f1b-ac8666352fae.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/95475d00-301c-4c9f-8f53-8a8879ecce06.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/9a1f6b76-c208-4e05-88f8-3063e80264c0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/9e57a389-3529-4355-85bb-710875e9ac36.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/a28ba1be-52a1-4b0f-9ef4-f6390977e4d9.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/adb8e4d7-24d0-47d1-b902-2063625d21e5.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/ae4823ea-5270-4b58-8bbf-8bb4ef30cb30.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/afd03065-caac-4fdc-ae2e-2b0f67445573.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/b495548a-1522-440b-91f7-d552ae3858b2.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/bc3d7b42-d780-4382-800c-2cd11de25180.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/c1fdc374-2a87-4b60-b1be-072b201635ea.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/c3fb3644-a7bb-4338-826c-f6553c5cddb7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/cab1c97a-0ff3-4356-b007-5cdc304770fc.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/caf48ff7-ad19-48e2-9b6b-dd7f5be2c1c1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/cb6099d5-f42c-4e6b-9bea-d7833925c8c0.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/cf85fa0a-f109-4589-a653-19acb940bb0a.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/d3407685-7101-4d1e-89ae-8f26ef91cdab.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/d349c7dc-dc6d-4dd7-a0fd-42470c96bce7.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/df767253-2d9a-4ac0-9b3a-921a131daaaf.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/e170784e-39da-4976-9b3a-7810c2228f9d.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/eff6786b-3dca-4b04-8eab-232c0838b9e1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/f90d02c7-b91e-4485-b83f-20c5f01ca265.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/fb0be5c5-d915-48d8-b746-4d2ca0ac72e1.root',
'/store/express/Commissioning2021/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/346/512/00000/fd7f6d5f-36ef-4a46-b5c5-0a33872297da.root'
] )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(int(-1 / 1)) )
process.source.skipEvents=cms.untracked.uint32(int(0*-1/1))



process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(False),
   Rethrow = cms.untracked.vstring("ProductNotFound"), # make this exception fatal
   fileMode  =  cms.untracked.string('NOMERGE') # no ordering needed, but calls endRun/beginRun etc. at file boundaries
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cout.enableStatistics = cms.untracked.bool(True)


process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")


process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.TrackRefitter.src = "ALCARECOTkAlMinBias"
process.TrackRefitter.TTRHBuilder = "WithAngleAndTemplate"
process.TrackRefitter.NavigationSchool = ""


#Global tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,"120X_dataRun3_Express_v2")


import CalibTracker.Configuration.Common.PoolDBESSource_cfi

process.conditionsInTrackerAlignmentRcd = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(
     connect = cms.string('sqlite_file:/afs/cern.ch/user/a/avagneri/MPproduction/mp3448/jobData/jobm/alignments_MP.db'),
     toGet = cms.VPSet(cms.PSet(record = cms.string('TrackerAlignmentRcd'),
                               tag = cms.string('Alignments')
                               )
                      )
    )
process.prefer_conditionsInTrackerAlignmentRcd = cms.ESPrefer("PoolDBESSource", "conditionsInTrackerAlignmentRcd")

process.conditionsInBeamSpotObjectsRcd = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(
     connect = cms.string('sqlite_file:/afs/cern.ch/work/f/fbrivio/public/BeamSpot/PilotBeam2021/ExpressBeamSpot/BeamSpotObjects_2021_PilotBeams_LumiBased_v1.db'),
     toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'),
                               tag = cms.string('BeamSpotObjects_2021_PilotBeams_LumiBased_v1')
                               )
                      )
    )
process.prefer_conditionsInBeamSpotObjectsRcd = cms.ESPrefer("PoolDBESSource", "conditionsInBeamSpotObjectsRcd")



HLTSel = False

###################################################################
#  Runs and events
###################################################################
runboundary = 1
isMultipleRuns=False
if(isinstance(runboundary, (list, tuple))):
     isMultipleRuns=True
     print("Multiple Runs are selected")

if(isMultipleRuns):
     process.source.firstRun = cms.untracked.uint32(int(runboundary[0]))
else:
     process.source.firstRun = cms.untracked.uint32(int(runboundary))


###################################################################
# The trigger filter module
###################################################################
from HLTrigger.HLTfilters.triggerResultsFilter_cfi import *
process.theHLTFilter = triggerResultsFilter.clone(
    triggerConditions = cms.vstring("*"),
    hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
    l1tResults = cms.InputTag( "" ),
    throw = cms.bool(False)
)

###################################################################
# PV refit
###################################################################
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import offlinePrimaryVertices 
process.offlinePrimaryVerticesFromRefittedTrks  = offlinePrimaryVertices.clone()
process.offlinePrimaryVerticesFromRefittedTrks.TrackLabel                                       = cms.InputTag("TrackRefitter") 
process.offlinePrimaryVerticesFromRefittedTrks.vertexCollections.maxDistanceToBeam              = 1
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxNormalizedChi2             = 20
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.minSiliconLayersWithHits      = 5
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxD0Significance             = 5.0
# as it was prior to https://github.com/cms-sw/cmssw/commit/c8462ae4313b6be3bbce36e45373aa6e87253c59
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxD0Error                    = 1.0
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.maxDzError                    = 1.0
process.offlinePrimaryVerticesFromRefittedTrks.TkFilterParameters.minPixelLayersWithHits        = 2   

# Use compressions settings of TFile
# see https://root.cern.ch/root/html534/TFile.html#TFile:SetCompressionSettings
# settings = 100 * algorithm + level
# level is from 1 (small) to 9 (large compression)
# algo: 1 (ZLIB), 2 (LMZA)
# see more about compression & performance: https://root.cern.ch/root/html534/guides/users-guide/InputOutput.html#compression-and-performance
compressionSettings = 207

###################################################################
# The PV resolution module
###################################################################
process.PrimaryVertexResolution = cms.EDAnalyzer('SplitVertexResolution',
                                                 compressionSettings = cms.untracked.int32(compressionSettings),
                                                 storeNtuple         = cms.bool(False),
                                                 vtxCollection       = cms.InputTag("offlinePrimaryVerticesFromRefittedTrks"),
                                                 trackCollection     = cms.InputTag("TrackRefitter"),		
                                                 minVertexNdf        = cms.untracked.double(10.),
                                                 minVertexMeanWeight = cms.untracked.double(0.5),
                                                 sumpTEndScale = cms.untracked.double(50.),
                                                 runControl = cms.untracked.bool(False),
                                                 runControlNumber = cms.untracked.vuint32(runboundary)
                                                 )



process.TFileService = cms.Service("TFileService",
    fileName = cms.string('PrimaryVertexResolution_run2021data_mp3448.root')
)




process.theValidSequence = cms.Sequence(process.offlineBeamSpot                        +
                                        process.TrackRefitter                          +
                                        process.offlinePrimaryVerticesFromRefittedTrks +
                                        process.PrimaryVertexResolution)
if (HLTSel):
    process.p = cms.Path(process.theHLTFilter + process.theValidSequence)
else:
    process.p = cms.Path(process.theValidSequence)


print("Done")
