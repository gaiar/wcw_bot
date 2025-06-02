import logging
import cv2
from proto_filter import * 

class instance(proto_filter):
    def get(self,tags,confidences,boxes,source_cfg=None,parameters = None):
        """ 
        gets tags,confidences,boxes
        returns filtered tags,confidences,boxes
        """
        logging.debug('Module "%s" activated.', __name__)
        min_confidence = self.main_cfg['general']['filtering']['min_confidence']
        nms_threshold = self.main_cfg['general']['filtering']['nms_threshold']

        if source_cfg and source_cfg.get('min_confidence'): min_confidence = source_cfg.get('min_confidence')
        if source_cfg and source_cfg.get('nms_threshold'):  nms_threshold = source_cfg.get('nms_threshold')

        if parameters and parameters.get('min_confidence'): min_confidence = parameters.get('min_confidence')
        if parameters and parameters.get('nms_threshold'):  nms_threshold = parameters.get('nms_threshold')

        indices = cv2.dnn.NMSBoxes(boxes, confidences, min_confidence, nms_threshold)
        res = []
        
        # Handle case where no objects pass the thresholds
        if indices is not None and len(indices) > 0:
            for idx in indices:
                # Handle OpenCV version compatibility
                if hasattr(idx, '__len__') and len(idx) > 0:
                    # Older OpenCV versions return 2D array [[index]]
                    idx = idx[0]
                # Newer OpenCV versions return flattened array [index]
                res.append( [tags[idx],confidences[idx],boxes[idx]] )
        
        if res:
            res = list(zip(*res))
        else:
            res = [[], [], []]
        logging.info('Module "%s": found tags %s.', __name__, str(res))
        return res        
